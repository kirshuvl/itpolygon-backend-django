from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.seminars.models import Seminar
from core.apps.steps.models import Step
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


class HomeworkStepConnection(TimedBaseModel):
    homework = models.ForeignKey(
        Homework,
        related_name="homework_step_connections",
        verbose_name="Семинар",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="homework_step_connections",
        verbose_name="Шаг",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ шага в семинаре",
        default=1000,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать?",
        default=False,
    )

    class Meta:
        verbose_name = "Домашнее задание -> Шаг"
        verbose_name_plural = "3. Домашние задания -> Шаги"
        ordering = ["pk"]
        db_table = "homework_step_connections"
        unique_together = (
            "homework",
            "step",
        )
