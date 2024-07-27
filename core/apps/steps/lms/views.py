from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from core.apps.steps.models import (
    QuestionStep,
    Step,
    UserStepBookmark,
    UserStepEnroll,
    UserStepLike,
)

from core.apps.steps.lms.serializers import (
    UserAnswerForProblemStepCreateSerializer,
    UserAnswerForQuestionStepCreateSerializer,
    UserStepBookmarkSerializer,
    UserStepEnrollCreateSerializer,
    UserStepEnrollRetrieveSerializer,
    UserStepLikeSerializer,
    UserStepViewSerializer,
)
from core.apps.steps.serializers import (
    UserAnswerForProblemStepCommonSerializer,
    UserAnswerForQuestionStepCommonSerializer,
)

from core.apps.steps.tasks import run_user_code


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepEnrolls Create",
)
class UserStepEnrollCreateAPIView(CreateAPIView):
    serializer_class = UserStepEnrollCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            instance = UserStepEnroll.objects.get(user=self.request.user, step=request.data["step"])
            serializer = UserStepEnrollRetrieveSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserStepEnroll.DoesNotExist:
            pass

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            UserStepEnrollRetrieveSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepEnrolls Update",
)
class UserStepEnrollsUpdateAPIVIew(RetrieveAPIView, UpdateAPIView):
    serializer_class = UserStepEnrollRetrieveSerializer
    lookup_url_kwarg = "enrollId"
    http_method_names = ["patch"]

    def get_queryset(self):
        return UserStepEnroll.objects.all()


@extend_schema(
    tags=["LMS"],
    summary="User Answer For Question Step Create",
)
class UserAnswerForQuestionStepCreateAPIView(CreateAPIView):
    serializer_class = UserAnswerForQuestionStepCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        answer = request.data.copy()
        question = QuestionStep.objects.get(pk=request.data["question"])
        user_answer = request.data["answer"]
        answer["is_correct"] = user_answer == question.answer

        serializer = self.get_serializer(data=answer)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        self.perform_create(serializer)
        enroll = UserStepEnroll.objects.get(user=self.request.user, step=question)
        if user_answer == question.answer:
            enroll.status = "OK"
        elif user_answer != question.answer and enroll.status != "OK":
            enroll.status = "WA"
        enroll.save()

        answer_data = UserAnswerForQuestionStepCommonSerializer(serializer.instance).data
        enroll_data = UserStepEnrollRetrieveSerializer(enroll).data

        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "answer": answer_data,
                "userEnroll": enroll_data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


@extend_schema(
    tags=["LMS"],
    summary="User Answer For Problem Step Create",
)
class UserAnswerForProblemStepCreateAPIView(CreateAPIView):
    serializer_class = UserAnswerForProblemStepCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        s = serializer.instance.problem
        enroll, _ = UserStepEnroll.objects.get_or_create(user=self.request.user, step=s)
        enroll.status = "WT"
        enroll.save()

        headers = self.get_success_headers(serializer.data)

        run_user_code.delay(serializer.instance.id)
        return Response(
            {
                "answer": UserAnswerForProblemStepCommonSerializer(serializer.instance).data,
                "userEnroll": UserStepEnrollRetrieveSerializer(enroll).data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepLikes Create",
)
class UserStepLikeCreateAPIView(CreateAPIView):
    serializer_class = UserStepLikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        print(serializer.data)
        step = Step.objects.get(pk=serializer.data["step"])

        return Response(
            {
                "userLike": {"id": serializer.data.get("id")},
                "liked_by": step.liked_by,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepLikes Delete",
)
class UserStepLikeDeleteAPIView(DestroyAPIView):
    serializer_class = UserStepLikeSerializer
    lookup_url_kwarg = "likeId"

    def get_queryset(self):
        return UserStepLike.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.step)

        id = instance.step.id
        self.perform_destroy(instance)
        step = Step.objects.get(pk=id)
        return Response(
            {
                "liked_by": step.liked_by,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepBookmarks Create",
)
class UserStepBookmarkCreateAPIView(CreateAPIView):
    serializer_class = UserStepBookmarkSerializer


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepBookmarks Delete",
)
class UserStepBookmarkDeleteAPIView(DestroyAPIView):
    serializer_class = UserStepBookmarkSerializer
    lookup_url_kwarg = "bookmarkId"

    def get_queryset(self):
        return UserStepBookmark.objects.filter(user=self.request.user)


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepViews Create",
)
class UserStepViewCreateAPIView(CreateAPIView):
    serializer_class = UserStepViewSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        print(serializer.data)
        step = Step.objects.get(pk=serializer.data["step"])

        return Response(
            {
                "viewed_by": step.viewed_by,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
