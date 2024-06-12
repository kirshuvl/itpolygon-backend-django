from django.contrib import admin

from core.apps.dashboard.models import UserCourseEnroll, UserHomeworkEnroll, UserSeminarEnroll


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


@admin.register(UserSeminarEnroll)
@admin.register(UserHomeworkEnroll)
class UserSeminarEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "seminar",
        "collection",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "user",
        "seminar",
        "collection",
    )
    search_fields = (
        "id",
        "user",
        "seminar",
        "collection",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "seminar",
        "collection",
    )
    ordering = ("id",)
