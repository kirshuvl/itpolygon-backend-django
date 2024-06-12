from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.collections.models import CollectionStepConnection
from core.apps.dashboard.models import UserHomeworkEnroll, UserSeminarEnroll
from core.apps.seminars.models import Seminar
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import (
    HomeworkListSerializer,
    HomeworkRetrieveSerializer,
    SeminarRetrieveSerializer,
    SeminarsListSerializer,
)


@extend_schema(
    tags=["LMS", "Dashboard"],
    summary="User Seminars List",
)
class SeminarListAPIView(ListAPIView):
    serializer_class = SeminarsListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Seminar.objects.prefetch_related(
                Prefetch(
                    "user_seminar_enrolls",
                    queryset=UserSeminarEnroll.objects.select_related("collection__course").filter(
                        user=self.request.user
                    ),
                ),
                Prefetch(
                    "user_seminar_enrolls__collection__colection_step_connections",
                    queryset=CollectionStepConnection.objects.prefetch_related(
                        Prefetch(
                            "step__user_step_enrolls",
                            queryset=UserStepEnroll.objects.filter(user=self.request.user),
                        )
                    )
                    .select_related(
                        "step",
                        "step__textstep",
                        "step__videostep",
                        "step__questionstep",
                        "step__problemstep",
                    )
                    .filter(is_published=True)
                    .order_by("number"),
                ),
            )
            .select_related("teacher")
            .filter(user_seminar_enrolls__user=self.request.user)
        )


@extend_schema(
    tags=["LMS", "Dashboard"],
    summary="User Homework List",
)
class HomeworkListAPIView(ListAPIView):
    serializer_class = HomeworkListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Seminar.objects.prefetch_related(
                Prefetch(
                    "user_homework_enrolls",
                    queryset=UserHomeworkEnroll.objects.select_related("collection__course").filter(
                        user=self.request.user
                    ),
                ),
                Prefetch(
                    "user_homework_enrolls__collection__colection_step_connections",
                    queryset=CollectionStepConnection.objects.prefetch_related(
                        Prefetch(
                            "step__user_step_enrolls",
                            queryset=UserStepEnroll.objects.filter(user=self.request.user),
                        )
                    )
                    .select_related(
                        "step",
                        "step__textstep",
                        "step__videostep",
                        "step__questionstep",
                        "step__problemstep",
                    )
                    .filter(is_published=True)
                    .order_by("number"),
                ),
            )
            .select_related("teacher")
            .filter(user_homework_enrolls__user=self.request.user)
        )


@extend_schema(
    tags=["LMS", "Screens"],
    summary="Seminar Retrieve",
)
class SeminarRetrieveAPIView(RetrieveAPIView):
    serializer_class = SeminarRetrieveSerializer
    lookup_url_kwarg = "seminarId"

    def get_queryset(self):
        return (
            Seminar.objects.prefetch_related(
                Prefetch(
                    "user_seminar_enrolls",
                    queryset=UserSeminarEnroll.objects.select_related("collection__course").filter(
                        user=self.request.user
                    ),
                ),
                Prefetch(
                    "user_seminar_enrolls__collection__colection_step_connections",
                    queryset=CollectionStepConnection.objects.prefetch_related(
                        Prefetch(
                            "step__user_step_enrolls",
                            queryset=UserStepEnroll.objects.filter(user=self.request.user),
                        )
                    )
                    .select_related(
                        "step",
                        "step__textstep",
                        "step__videostep",
                        "step__questionstep",
                        "step__problemstep",
                    )
                    .filter(is_published=True)
                    .order_by("number"),
                ),
            )
            .select_related("teacher")
            .filter(user_seminar_enrolls__user=self.request.user)
        )


@extend_schema(
    tags=["LMS", "Screens"],
    summary="Homework Retrieve",
)
class HomeworkRetrieveAPIView(RetrieveAPIView):
    serializer_class = HomeworkRetrieveSerializer
    lookup_url_kwarg = "homeworkId"

    def get_queryset(self):
        return (
            Seminar.objects.prefetch_related(
                Prefetch(
                    "user_homework_enrolls",
                    queryset=UserHomeworkEnroll.objects.select_related("collection__course").filter(
                        user=self.request.user
                    ),
                ),
                Prefetch(
                    "user_homework_enrolls__collection__colection_step_connections",
                    queryset=CollectionStepConnection.objects.prefetch_related(
                        Prefetch(
                            "step__user_step_enrolls",
                            queryset=UserStepEnroll.objects.filter(user=self.request.user),
                        )
                    )
                    .select_related(
                        "step",
                        "step__textstep",
                        "step__videostep",
                        "step__questionstep",
                        "step__problemstep",
                    )
                    .filter(is_published=True)
                    .order_by("number"),
                ),
            )
            .select_related("teacher")
            .filter(user_homework_enrolls__user=self.request.user)
        )
