from django.contrib import admin

from core.apps.seminars.models import Seminar


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "date",
    )

    search_fields = (
        "id",
        "date",
        "created_at",
        "updated_at",
    )

    list_filter = ("date",)

    ordering = ("id",)
