from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.models import Course
from core.apps.groups.models import Group
from core.apps.homeworks.models import Homework
from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser


class UserCourseEnroll(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        related_name="user_course_enrolls",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        related_name="user_course_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name="user_course_enrolls",
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Студент -> Курс"
        verbose_name_plural = "1. Студенты -> Курсы"
        ordering = ("pk",)
        unique_together = (
            "user",
            "course",
            "group",
        )
        db_table = "user_course_enrolls"

    def __str__(self) -> str:
        return f"{self.course} -> {self.user}"


class UserSeminarEnroll(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        related_name="user_seminar_enrolls",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    seminar = models.ForeignKey(
        Seminar,
        related_name="user_seminar_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name="user_seminar_enrolls",
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        related_name="user_seminar_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Студент -> Семинар"
        verbose_name_plural = "2. Студенты -> Семинары"
        ordering = ("pk",)
        unique_together = (
            "user",
            "seminar",
            "group",
        )
        db_table = "user_seminar_enrolls"

    def __str__(self) -> str:
        return f"{self.seminar} -> {self.user}"


class UserHomeworkEnroll(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        related_name="user_homework_enrolls",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    homework = models.ForeignKey(
        Homework,
        related_name="user_homework_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name="user_homework_enrolls",
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Студент -> Домашнее задание"
        verbose_name_plural = "2. Студенты -> Домашние задания"
        ordering = ("pk",)
        unique_together = (
            "user",
            "homework",
            "group",
        )
        db_table = "user_homework_enrolls"

    def __str__(self) -> str:
        return f"{self.homework} -> {self.user}"
