from django.contrib import admin

from core.apps.dashboard.models import (
    UserCourseEnroll,
    # UserSeminarHomeworkEnroll,
    # UserSeminarEnroll,
)


@admin.register(UserCourseEnroll)
class UserCourseEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "course",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "user",
        "course",
    )
    search_fields = (
        "id",
        "user",
        "course",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "course",
    )
    ordering = ("id",)


"""
@admin.register(UserSeminarEnroll)
class UserSeminarEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "seminar",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "user",
        "seminar",
    )
    search_fields = (
        "id",
        "user",
        "seminar",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "seminar",
    )
    ordering = ("id",)


@admin.register(UserSeminarHomeworkEnroll)
class UserSeminarHomeworkEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "homework",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "user",
        "homework",
    )
    search_fields = (
        "id",
        "user",
        "homework",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "homework",
    )
    ordering = ("id",)
"""
