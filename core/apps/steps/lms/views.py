from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from core.apps.steps.models import QuestionStep, UserStepEnroll

from core.apps.steps.lms.serializers import (
    UserAnswerForQuestionStepCreateSerializer,
    UserAnswerForQuestionStepRetrieveSerializer,
    UserStepEnrollCreateSerializer,
    UserStepEnrollRetrieveSerializer,
)


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
        self.perform_create(serializer)

        enroll = UserStepEnroll.objects.get(user=self.request.user, step=question)
        if user_answer == question.answer:
            enroll.status = "OK"
        elif user_answer != question.answer and enroll.status != "OK":
            enroll.status = "WA"
        enroll.save()

        answer_data = UserAnswerForQuestionStepRetrieveSerializer(serializer.instance).data
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
