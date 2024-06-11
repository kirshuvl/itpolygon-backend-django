from django.db import models

from core.apps.collections.models import Collection
from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser


class Seminar(TimedBaseModel):

    date = models.DateTimeField(
        verbose_name="Дата занятия",
    )

    teacher = models.ForeignKey(
        CustomUser,
        related_name="teacher_seminar_enrolls",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Семинар"
        verbose_name_plural = "1. Семинары"
        ordering = ["pk"]
        db_table = "seminars"

    def __str__(self) -> str:
        return f"Дата: {self.date}"


class CollectionSeminarConnection(TimedBaseModel):
    collection = models.ForeignKey(
        Collection,
        related_name="collection_seminar_connections",
        verbose_name="Задание",
        on_delete=models.CASCADE,
    )

    seminar = models.ForeignKey(
        Seminar,
        related_name="collection_seminar_connections",
        verbose_name="Семинар",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Семинар -> Коллекция задания"
        verbose_name_plural = "2. Семинары -> Коллекции заданий"
        ordering = ["pk"]
        unique_together = (
            "collection",
            "seminar",
        )
        db_table = "collection_seminar_connections"

    def __str__(self) -> str:
        return f"{self.homework} -> {self.seminar}"
