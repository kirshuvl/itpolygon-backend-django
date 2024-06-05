from rest_framework.generics import ListAPIView

from core.apps.seminars.models import Seminar, TeacherSeminarEnroll
from django.db.models import Prefetch

from core.apps.seminars.lms.serializers import SeminarsListSerializer


class SeminarsListAPIView(ListAPIView):
    serializer_class = SeminarsListSerializer

    def get_queryset(self):
        return Seminar.objects.prefetch_related(
            Prefetch(
                "teacher_seminar_enrolls",
                queryset=TeacherSeminarEnroll.objects.select_related("teacher"),
            )
        ).filter(user_seminar_enrolls__user=self.request.user)
