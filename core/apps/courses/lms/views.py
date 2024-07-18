from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.apps.courses.models import Course, Lesson, LessonStepConnection, Topic
from core.apps.steps.models import (
    AnswerForSingleChoiceQuestionStep,
    TestForProblemStep,
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserAnswerForSingleChoiceQuestionStep,
    UserStepEnroll,
)
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
                    queryset=Topic.objects.filter(
                        is_published=True,
                    ).order_by("number"),
                ),
                Prefetch(
                    "topics__lessons",
                    queryset=Lesson.objects.filter(
                        is_published=True,
                    ).order_by("number"),
                ),
                Prefetch(
                    "topics__lessons__lesson_step_connections",
                    queryset=LessonStepConnection.objects.prefetch_related(
                        Prefetch(
                            "step__user_step_enrolls",
                            queryset=UserStepEnroll.objects.filter(
                                user=self.request.user,
                            ),
                        )
                    )
                    .select_related(
                        "step",
                        "step__textstep",
                        "step__videostep",
                        "step__questionstep",
                        "step__problemstep",
                        "step__singlechoicequestionstep",
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
                        queryset=UserStepEnroll.objects.filter(
                            user=self.request.user,
                        ),
                    )
                )
                .select_related(
                    "step",
                    "step__textstep",
                    "step__videostep",
                    "step__questionstep",
                    "step__problemstep",
                    "step__singlechoicequestionstep",
                )
                .prefetch_related(
                    Prefetch(
                        "step__questionstep__user_answer_for_question_steps",
                        queryset=UserAnswerForQuestionStep.objects.filter(
                            user=self.request.user,
                        ),
                    )
                )
                .prefetch_related(
                    Prefetch(
                        "step__singlechoicequestionstep__answer_for_single_choice_question_steps",
                        queryset=AnswerForSingleChoiceQuestionStep.objects.all(),
                    )
                )
                .prefetch_related(
                    Prefetch(
                        "step__singlechoicequestionstep__user_answer_for_single_choice_question_steps",  # noqa
                        queryset=UserAnswerForSingleChoiceQuestionStep.objects.filter(
                            user=self.request.user,
                        ),
                    )
                )
                .prefetch_related(
                    Prefetch(
                        "step__problemstep__user_answer_for_problem_steps",
                        queryset=UserAnswerForProblemStep.objects.filter(user=self.request.user),
                    )
                )
                .prefetch_related(
                    Prefetch(
                        "step__problemstep__tests",
                        queryset=TestForProblemStep.objects.order_by("number"),
                    )
                )
                .order_by("number"),
            )
        )
