from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from core.apps.seminars.models import Seminar, SeminarStepConnection, TeacherSeminarEnroll
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import SeminarsListSerializer


class SeminarMixinAPIView:
    def get_queryset(self):
        return Seminar.objects.prefetch_related(
            Prefetch(
                "teacher_seminar_enrolls",
                queryset=TeacherSeminarEnroll.objects.select_related("teacher"),
            ),
            Prefetch(
                "seminar_step_connections",
                queryset=SeminarStepConnection.objects.prefetch_related(
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
        ).filter(user_seminar_enrolls__user=self.request.user)


@extend_schema(
    tags=["LMS"],
    summary="User Seminars List",
)
class SeminarListAPIView(SeminarMixinAPIView, ListAPIView):
    serializer_class = SeminarsListSerializer


@extend_schema(
    tags=["LMS"],
    summary="User Seminar Retrieve",
)
class SeminarRetrieveAPIView(SeminarMixinAPIView, ListAPIView):
    serializer_class = SeminarsListSerializer
    lookup_url_kwarg = "seminarId"
