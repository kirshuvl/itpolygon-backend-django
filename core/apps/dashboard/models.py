from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.models import Course
from core.apps.groups.models import Group
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
        )
        db_table = "user_course_enrolls"

    def __str__(self) -> str:
        return f"{self.course} -> {self.user}"
