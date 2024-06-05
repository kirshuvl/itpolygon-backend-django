from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.steps.models import Step
from core.apps.users.models import CustomUser


class Seminar(TimedBaseModel):

    date = models.DateTimeField(
        verbose_name="Дата занятия",
    )

    class Meta:
        verbose_name = "Семинар"
        verbose_name_plural = "1. Семинары"
        ordering = ["pk"]
        db_table = "seminars"

    def __str__(self) -> str:
        return f"Дата: {self.date}"


class TeacherSeminarEnroll(TimedBaseModel):
    teacher = models.ForeignKey(
        CustomUser,
        related_name="teacher_seminar_enrolls",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    seminar = models.ForeignKey(
        Seminar,
        related_name="teacher_seminar_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Семинар -> Преподаватель"
        verbose_name_plural = "2. Семинары -> Преподаватели"
        ordering = ["pk"]
        unique_together = (
            "teacher",
            "seminar",
        )
        db_table = "teacher_seminar_enrolls"

    def __str__(self) -> str:
        return f"{self.seminar} -> {self.teacher}"


class SeminarStepConnection(TimedBaseModel):
    seminar = models.ForeignKey(
        Seminar,
        related_name="seminar_step_connections",
        verbose_name="Семинар",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="seminar_step_connections",
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
        verbose_name = "Семинар -> Шаг"
        verbose_name_plural = "3. Семинары -> Шаги"
        ordering = ["pk"]
        db_table = "seminar_step_connections"
        unique_together = (
            "seminar",
            "step",
        )
