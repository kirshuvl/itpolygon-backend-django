from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.courses.models import Course
from core.apps.steps.models import Step
from core.apps.users.models import CustomUser


class Collection(TimedBaseModel):
    author = models.ForeignKey(
        CustomUser,
        related_name="collections",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        related_name="collections",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Коллекция заданий"
        verbose_name_plural = "1. Коллекции заданий"
        ordering = ["pk"]
        db_table = "collections"

    def __str__(self) -> str:
        return f"Коллекция заданий № {self.pk}"


class CollectionStepConnection(TimedBaseModel):
    collection = models.ForeignKey(
        Collection,
        related_name="collection_step_connections",
        verbose_name="Коллекция заданий",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="collection_step_connections",
        verbose_name="Шаг",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ шага в коллекции",
        default=1000,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    class Meta:
        verbose_name = "Коллекция заданий -> Шаг"
        verbose_name_plural = "2. Коллекции заданий -> Шаги"
        ordering = ["pk"]
        db_table = "collection_step_connections"
        unique_together = (
            "collection",
            "step",
            "number",
        )

    def __str__(self) -> str:
        return f"{self.collection} -> {self.step}"
