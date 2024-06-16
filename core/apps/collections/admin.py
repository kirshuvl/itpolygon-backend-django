from django.contrib import admin

from core.apps.collections.models import Collection, CollectionStepConnection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
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


@admin.register(CollectionStepConnection)
class CollectionStepConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "collection",
        "step",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "collection",
        "step",
    )

    search_fields = (
        "id",
        "collection",
        "step",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "collection",
        "step",
        "is_published",
    )

    ordering = ("id",)
