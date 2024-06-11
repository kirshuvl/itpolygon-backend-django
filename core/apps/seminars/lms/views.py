from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.dashboard.models import UserHomeworkEnroll, UserSeminarEnroll
from core.apps.seminars.models import Seminar
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import HomeworkListSerializer, SeminarsListSerializer


@extend_schema(
    tags=["LMS"],
    summary="User Seminars Listddd",
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
            )
            .select_related("teacher")
            .filter(user_seminar_enrolls__user=self.request.user)
        )


@extend_schema(
    tags=["LMS"],
    summary="User Homework List",
)
class HomeworkListAPIView(ListAPIView):
    serializer_class = HomeworkListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Seminar.objects.prefetch_related(
                Prefetch(
                    "user_seminar_enrolls",
                    queryset=UserHomeworkEnroll.objects.select_related("collection__course").filter(
                        user=self.request.user
                    ),
                ),
            )
            .select_related("teacher")
            .filter(user_homework_enrolls__user=self.request.user)
        )
