from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser


class Group(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название группы",
        max_length=255,
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "1. Группы"
        ordering = ("pk",)
        db_table = "groups"

    def __str__(self) -> str:
        return self.title


class StudentGroupEnroll(TimedBaseModel):
    student = models.ForeignKey(
        CustomUser,
        related_name="student_group_enrolls",
        verbose_name="Студент",
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name="student_group_enrolls",
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Группа -> Студент"
        verbose_name_plural = "2. Группы -> Студенты"
        ordering = ("pk",)
        unique_together = (
            "group",
            "student",
        )
        db_table = "student_group_enrolls"

    def __str__(self) -> str:
        return f"{self.student} -> {self.group}"


class TeacherGroupEnroll(TimedBaseModel):
    teacher = models.ForeignKey(
        CustomUser,
        related_name="teacher_group_enrolls",
        verbose_name="Студент",
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name="teacher_group_enrolls",
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Группа -> Преподаватель"
        verbose_name_plural = "3. Группы -> Преподаватели"
        ordering = ("pk",)
        unique_together = (
            "group",
            "teacher",
        )
        db_table = "teacher_group_enrolls"

    def __str__(self) -> str:
        return f"{self.teacher} -> {self.group}"
