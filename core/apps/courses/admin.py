from django.contrib import admin

from core.apps.courses.models import AuthorCourseEnroll, Course, Lesson, Topic


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
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


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
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


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
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


@admin.register(AuthorCourseEnroll)
class AuthorCourseEnrollAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course",
        "author",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "course",
        "author",
    )
    search_fields = (
        "id",
        "course",
        "author",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "course",
        "author",
    )
    ordering = ("id",)
