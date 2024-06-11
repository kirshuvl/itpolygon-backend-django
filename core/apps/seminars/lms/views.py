from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.dashboard.models import UserSeminarEnroll
from core.apps.seminars.models import Seminar
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import SeminarsListSerializer


@extend_schema(
    tags=["LMS"],
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
            )
            .select_related("teacher")
            .filter(user_seminar_enrolls__user=self.request.user)
        )
