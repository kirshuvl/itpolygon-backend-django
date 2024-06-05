from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser


class Homework(TimedBaseModel):
    author = models.ForeignKey(
        CustomUser,
        related_name="homeworks",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    seminar = models.ForeignKey(
        Seminar,
        related_name="homeworks",
        verbose_name="Семинар",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "1. Домашние задания"
        ordering = ["pk"]
        db_table = "homeworks"
