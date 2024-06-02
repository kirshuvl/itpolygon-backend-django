from django.contrib import admin

from core.apps.steps.models import (
    ProblemStep,
    QuestionStep,
    Step,
    TextStep,
    UserAnswerForQuestionStep,
    UserStepEnroll,
    VideoStep,
)


@admin.register(Step)
@admin.register(TextStep)
@admin.register(VideoStep)
@admin.register(QuestionStep)
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