from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "status",
        "created_at",
        "updated_at",
    )

    list_display_links = (
        "id",
        "first_name",
        "last_name",
        "email",
    )

    search_fields = (
        "id",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = ("status",)

    fieldsets = (
        (
            "Основная информация",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "icon",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "status",
                ),
            },
        ),
        (
            "Пароль",
            {
                "classes": ("wide",),
                "fields": ("password",),
            },
        ),
    )

    add_fieldsets = (
        (
            "Создать пользователя",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )

    ordering = ("id",)
