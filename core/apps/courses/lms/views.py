from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.courses.models import Course, Lesson, LessonStepConnection, Topic
from core.apps.steps.models import UserStepEnroll
from django.db.models import Prefetch

from core.apps.courses.lms.serializers import (
    CourseListSerializer,
    CourseRetrieveSerializer,
    LessonRetrieveSerializer,
)


class CourseMixinAPIView:
    def get_queryset(self):
        return (
            Course.objects.prefetch_related(
                Prefetch(
                    "topics",
                    queryset=Topic.objects.filter(is_published=True).order_by("number"),
                ),
                Prefetch(
                    "topics__lessons",
                    queryset=Lesson.objects.filter(is_published=True).order_by("number"),
                ),
                Prefetch(
                    "topics__lessons__lesson_step_connections",
                    queryset=LessonStepConnection.objects.prefetch_related(
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
            .filter(
                user_course_enrolls__user=self.request.user,
                is_published=True,
            )
            .distinct()
        )


@extend_schema(
    tags=["LMS", "Dashboard"],
    summary="User Courses List",
)
class CourseListAPIView(CourseMixinAPIView, ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    tags=["LMS"],
    summary="User Course Retrieve",
)
class CourseRetrieveAPIView(CourseMixinAPIView, RetrieveAPIView):
    serializer_class = CourseRetrieveSerializer
    lookup_url_kwarg = "courseId"


@extend_schema(
    tags=["LMS", "Screens"],
    summary="Lesson Retrieve",
)
class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonRetrieveSerializer
    lookup_url_kwarg = "lessonId"

    def get_queryset(self):
        return Lesson.objects.prefetch_related(
            Prefetch(
                "lesson_step_connections",
                queryset=LessonStepConnection.objects.prefetch_related(
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
                .order_by("number"),
            )
        )
