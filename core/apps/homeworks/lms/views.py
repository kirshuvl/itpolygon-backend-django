from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.apps.homeworks.models import Homework, HomeworkStepConnection
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.homeworks.lms.serializers import HomeworkSerializer


class HomeworkMixinAPIView:
    def get_queryset(self):
        return Homework.objects.select_related(
            "author",
            "seminar",
        ).prefetch_related(
            Prefetch(
                "homework_step_connections",
                queryset=HomeworkStepConnection.objects.prefetch_related(
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
    summary="User Homeworks List",
)
class HomeworkListAPIView(HomeworkMixinAPIView, ListAPIView):
    serializer_class = HomeworkSerializer


@extend_schema(
    tags=["LMS"],
    summary="User Homework Retrieve",
)
class HomeworkRetrieveAPIView(HomeworkMixinAPIView, RetrieveAPIView):
    serializer_class = HomeworkSerializer
    lookup_url_kwarg = "homeworkId"
