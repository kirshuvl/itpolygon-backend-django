from django.contrib import admin

from core.apps.homeworks.models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "author",
    )
    search_fields = (
        "id",
        "author",
        "created_at",
        "updated_at",
    )
    list_filter = ("author",)
    ordering = ("id",)
