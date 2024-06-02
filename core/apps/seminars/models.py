from django.db import models

from core.apps.common.models import TimedBaseModel


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
        return f"Курс: {self.course} | Дата: {self.date}"
