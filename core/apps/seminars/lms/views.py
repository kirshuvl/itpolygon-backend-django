from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.seminars.models import Seminar, TeacherSeminarEnroll
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import SeminarsListSerializer, SeminarsRetrieveSerializer


@extend_schema(
    tags=["LMS"],
    summary="User Seminars List",
)
class SeminarListAPIView(ListAPIView):
    serializer_class = SeminarsListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Seminar.objects.prefetch_related(
            Prefetch(
                "teacher_seminar_enrolls",
                queryset=TeacherSeminarEnroll.objects.select_related("teacher"),
            ),
            "user_seminar_enrolls__course",
        ).filter(user_seminar_enrolls__user=self.request.user)


@extend_schema(
    tags=["LMS"],
    summary="User Seminar Retrieve",
)
class SeminarRetrieveAPIView(RetrieveAPIView):

    serializer_class = SeminarsRetrieveSerializer
    lookup_url_kwarg = "seminarId"

    def get_queryset(self):
        return Seminar.objects.prefetch_related(
            Prefetch(
                "teacher_seminar_enrolls",
                queryset=TeacherSeminarEnroll.objects.select_related("teacher"),
            ),
        ).filter(user_seminar_enrolls__user=self.request.user)
