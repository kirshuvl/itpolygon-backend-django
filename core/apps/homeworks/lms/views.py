from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from core.apps.homeworks.models import Homework

from core.apps.homeworks.lms.serializers import HomeworksListSerializer


@extend_schema(
    tags=["LMS"],
    summary="User Homeworks List",
)
class HomeworksListAPIView(ListAPIView):
    serializer_class = HomeworksListSerializer

    def get_queryset(self):
        return Homework.objects.select_related(
            "author",
            "seminar",
        ).all()
