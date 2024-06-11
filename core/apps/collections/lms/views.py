from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.collections.models import Collection, CollectionStepConnection
from core.apps.dashboard.models import UserSeminarEnroll
from core.apps.seminars.models import Seminar
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.collections.lms.serializers import HomeworkSerializer


class HomeworkMixinAPIView:
    def get_queryset(self):
        return Collection.objects.select_related(
            "author",
            "seminar",
        ).prefetch_related(
            Prefetch(
                "homework_step_connections",
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


@extend_schema(
    tags=["LMS"],
    summary="User Homework Retrieve",
)
class HomeworkRetrieveAPIView(HomeworkMixinAPIView, RetrieveAPIView):
    serializer_class = HomeworkSerializer
    lookup_url_kwarg = "homeworkId"


@extend_schema(
    tags=["LMS"],
    summary="Course Homework List",
)
class CourseHomeworkListAPIView(HomeworkMixinAPIView, ListAPIView):
    serializer_class = HomeworkSerializer
