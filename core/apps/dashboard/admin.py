from django.contrib import admin

from core.apps.dashboard.models import UserCourseEnroll


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
