from django.contrib import admin

from core.apps.groups.models import Group, StudentGroupEnroll, TeacherGroupEnroll


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
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
        "created_at",
        "updated_at",
    )
    list_filter = ("title",)
    ordering = ("id",)


@admin.register(StudentGroupEnroll)
class StudentGroupEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "group",
        "student",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "group",
        "student",
    )
    search_fields = (
        "id",
        "group",
        "student",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "group",
        "student",
    )
    ordering = ("id",)


@admin.register(TeacherGroupEnroll)
class TeacherGroupEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "group",
        "teacher",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "group",
        "teacher",
    )
    search_fields = (
        "id",
        "group",
        "teacher",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "group",
        "teacher",
    )
    ordering = ("id",)
