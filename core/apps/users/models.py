from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.common.models import TimedBaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.apps.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, TimedBaseModel):
    username = None

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=30,
    )

    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=30,
    )

    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        unique=True,
        error_messages={"unique": "Пользователь с такой почтой уже зарегистрировался"},
    )

    icon = models.ImageField(
        verbose_name="Фотография профиля",
        upload_to="icon/user/",
        blank=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    STATUS_CHOICES = [
        ("teacher", "Преподаватель"),
        ("student", "Студент"),
    ]

    status = models.CharField(
        verbose_name="Статус",
        max_length=7,
        choices=STATUS_CHOICES,
        default="student",
        blank=True,
    )

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь [Сайт]"
        verbose_name_plural = "1. Пользователи [Сайт]"
        ordering = ["pk"]
        db_table = "custom_users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
