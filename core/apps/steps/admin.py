from django.contrib import admin

from core.apps.steps.models import (
    AnswerForSingleChoiceQuestionStep,
    ProblemStep,
    QuestionStep,
    SingleChoiceQuestionStep,
    Step,
    TestForProblemStep,
    TextStep,
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserAnswerForSingleChoiceQuestionStep,
    UserAnswerForTestForProblemStep,
    UserStepBookmark,
    UserStepEnroll,
    UserStepLike,
    UserStepView,
    VideoStep,
)


@admin.register(Step)
@admin.register(TextStep)
@admin.register(VideoStep)
@admin.register(QuestionStep)
@admin.register(SingleChoiceQuestionStep)
@admin.register(ProblemStep)
class StepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "title",
    )

    search_fields = (
        "id",
        "title",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "title",
        "is_published",
    )

    ordering = ("id",)


@admin.register(UserAnswerForQuestionStep)
class UserAnswerForQuestionStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "question",
        "answer",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "user",
        "question",
        "answer",
    )

    search_fields = (
        "id",
        "user",
        "question",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "user",
        "question",
    )

    ordering = ("id",)


@admin.register(TestForProblemStep)
class TestForProblemStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "problem",
        "number",
        "input",
        "output",
    )

    list_display_links = (
        "id",
        "problem",
        "number",
        "input",
        "output",
    )

    search_fields = (
        "id",
        "problem",
        "number",
        "input",
        "output",
    )

    list_filter = ("problem",)

    ordering = ("id",)


@admin.register(UserAnswerForProblemStep)
class UserAnswerForProblemStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "verdict",
    )

    list_display_links = (
        "id",
        "user",
        "verdict",
    )

    search_fields = (
        "id",
        "user",
        "verdict",
    )


@admin.register(AnswerForSingleChoiceQuestionStep)
class AnswerForSingleChoiceQuestionStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
        "answer",
        "is_correct",
    )

    list_display_links = (
        "id",
        "question",
    )

    list_filter = (
        "id",
        "question",
    )


@admin.register(UserStepEnroll)
class UserStepEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "step",
        "user",
        "status",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "step",
        "user",
    )

    search_fields = (
        "id",
        "step",
        "user",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "step",
        "user",
    )

    ordering = ("id",)


@admin.register(UserAnswerForTestForProblemStep)
class UserAnswerForTestForProblemStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "verdict",
    )

    list_display_links = (
        "id",
        "user",
        "verdict",
    )

    search_fields = (
        "id",
        "user",
        "verdict",
    )


@admin.register(UserStepLike)
@admin.register(UserStepBookmark)
@admin.register(UserStepView)
class UserStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "step",
        "user",
        "source",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "step",
        "user",
    )

    search_fields = (
        "id",
        "step",
        "user",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "step",
        "user",
    )

    ordering = ("id",)


@admin.register(UserAnswerForSingleChoiceQuestionStep)
class UserAnswerForSingleChoiceQuestionStepAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "question",
        "answer",
        "is_correct",
    )

    list_display_links = (
        "id",
        "user",
        "question",
    )
