from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.models import Course
from core.apps.steps.models import Step
from core.apps.users.models import CustomUser


class Homework(TimedBaseModel):
    author = models.ForeignKey(
        CustomUser,
        related_name="homeworks",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        related_name="homeworks",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )
    STATUS_CHOICES = [
        ("HW", "Домашнее задание"),
        ("SN", "Задание на семинар"),
    ]
    status = models.CharField(
        verbose_name="Статус",
        max_length=2,
        choices=STATUS_CHOICES,
        default="HW",
        blank=True,
    )

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "1. Домашние задания"
        ordering = ["pk"]
        db_table = "homeworks"

    def __str__(self) -> str:
        return f"Домашнее задание № {self.pk} | {self.status}"


class HomeworkStepConnection(TimedBaseModel):
    homework = models.ForeignKey(
        Homework,
        related_name="homework_step_connections",
        verbose_name="Домашнее задание",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="homework_step_connections",
        verbose_name="Шаг",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ шага в домашнем задании",
        default=1000,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    class Meta:
        verbose_name = "Домашнее задание -> Шаг"
        verbose_name_plural = "2. Домашние задания -> Шаги"
        ordering = ["pk"]
        db_table = "homework_step_connections"
        unique_together = (
            "homework",
            "step",
        )
