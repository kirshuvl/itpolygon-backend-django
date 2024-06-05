from django.db import models

from core.apps.common.models import TimedBaseModel
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
