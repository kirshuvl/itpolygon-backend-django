from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser


class StepManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("textstep", "videostep", "questionstep", "problemstep")
        )


class DefaultStepManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("step_ptr")


class Step(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название шага",
        max_length=50,
        null=True,
        blank=True,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    objects = StepManager()

    class Meta:
        verbose_name = "Шаг"
        verbose_name_plural = "1. Шаги"
        ordering = ["pk"]
        db_table = "steps"

    def __str__(self) -> str:
        return f"{self.get_type()} № {self.pk}"

    def get_type(self):
        if hasattr(self, "textstep"):
            return "textstep"
        elif hasattr(self, "videostep"):
            return "videostep"
        elif hasattr(self, "questionstep"):
            return "questionstep"
        elif hasattr(self, "problemstep"):
            return "problemstep"
        return "None"


class TextStep(Step):
    text = models.JSONField(
        verbose_name="Текст",
    )

    objects = DefaultStepManager()

    class Meta:
        verbose_name = "Шаг [Текстовый]"
        verbose_name_plural = "2. Шаги [Текстовые]"
        ordering = ["pk"]
        db_table = "text_steps"


class VideoStep(Step):
    video_url = models.URLField(
        verbose_name="Ссылка на видео",
        max_length=500,
    )

    objects = DefaultStepManager()

    class Meta:
        verbose_name = "Шаг [Видео]"
        verbose_name_plural = "3. Шаги [Видео]"
        ordering = ["pk"]
        db_table = "video_steps"


class QuestionStep(Step):
    text = models.JSONField(
        verbose_name="Текст",
    )
    answer = models.CharField(
        verbose_name="Ответ",
    )

    objects = DefaultStepManager()

    class Meta:
        verbose_name = "Шаг [Вопрос]"
        verbose_name_plural = "4. Шаги [Вопрос]"
        ordering = ["pk"]
        db_table = "question_steps"


class UserAnswerForQuestionStep(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        related_name="question_answers",
        verbose_name="Пользователь",
        on_delete=models.PROTECT,
    )

    question = models.ForeignKey(
        Step,
        related_name="question_answers",
        verbose_name="Вопрос",
        on_delete=models.CASCADE,
    )

    answer = models.CharField(
        verbose_name="Ответ пользователя",
    )
    is_correct = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = "Шаг [Вопрос][Ответ]"
        verbose_name_plural = "4. Шаги [Вопрос] -> [Ответ]"
        ordering = ["pk"]
        db_table = "user_answers_for_question_steps"


class ProblemStep(Step):
    text = models.JSONField(
        verbose_name="Текст",
    )

    input = models.JSONField(
        verbose_name="Текст",
    )

    output = models.JSONField(
        verbose_name="Текст",
    )

    notes = models.JSONField(
        verbose_name="Текст",
    )

    start_code = models.TextField(
        verbose_name="Дополнительный код",
        max_length=10000,
        blank=True,
        default="",
    )

    first_sample = models.IntegerField(
        verbose_name="Первый сэмпл",
        default=1,
    )

    last_sample = models.IntegerField(
        verbose_name="Последний сэмпл",
        default=3,
    )

    first_test = models.IntegerField(
        verbose_name="Первый тест",
        default=4,
    )

    cputime = models.IntegerField(
        verbose_name="CPU Time",
        default=1,
    )

    memory = models.IntegerField(
        verbose_name="Memory",
        default=64,
    )

    objects = DefaultStepManager()

    class Meta:
        verbose_name = "Шаг [Программирование]"
        verbose_name_plural = "5. Шаги [Программирование]"
        ordering = ["pk"]
        db_table = "problem_steps"


class TestForProblemStep(TimedBaseModel):
    problem = models.ForeignKey(
        ProblemStep,
        related_name="tests",
        verbose_name="Задача",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ теста",
        default=1000,
    )

    input = models.TextField(
        verbose_name="Входные данные",
        max_length=100000,
        blank=True,
    )

    output = models.TextField(
        verbose_name="Выходные данные",
        max_length=100000,
        blank=True,
    )

    class Meta:
        verbose_name = "Шаг [Программирование][Тест]"
        verbose_name_plural = "5. Шаги [Программирование][Тесты]"
        ordering = ["pk"]
        unique_together = ("problem", "number")


class UserAnswerForProblemStep(TimedBaseModel):
    code = models.TextField(
        verbose_name="Код пользователя",
        max_length=10000,
    )
    user = models.ForeignKey(
        CustomUser,
        related_name="codes",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    problem = models.ForeignKey(
        ProblemStep,
        related_name="codes",
        verbose_name="Задача",
        on_delete=models.CASCADE,
    )

    LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("cpp", "C++"),
    ]
    language = models.CharField(
        verbose_name="Язык программирования",
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default="python",
    )
    VERDICT_CHOICES = [
        ("PR", "На проверке"),
        ("OK", "OK"),
        ("CE", "Ошибка компиляции"),
        ("WA", "Неправильный ответ"),
        ("TL", "Превышение времени"),
        ("ML", "Превышение памяти"),
        ("UN", "Незвестная ошибка"),
    ]
    verdict = models.CharField(
        verbose_name="Вердикт",
        max_length=2,
        choices=VERDICT_CHOICES,
        default="PR",
    )
    cputime = models.FloatField(
        verbose_name="CPU Time",
        default=0,
    )
    first_fail_test = models.IntegerField(
        verbose_name="Первый ошибочный тест",
        default=0,
    )
    points = models.IntegerField(
        verbose_name="Баллы",
        default=0,
    )

    class Meta:
        verbose_name = "Попытка пользователя"
        verbose_name_plural = "5. Шаги [Программирование] -> [Ответ]"
        ordering = ["pk"]


class UserStepEnroll(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        related_name="user_step_enrolls",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="user_step_enrolls",
        verbose_name="Шаг",
        on_delete=models.CASCADE,
    )

    STATUS_CHOICES = [
        ("PR", "Шаг изучается"),
        ("RP", "Шаг повторяется"),
        ("WA", "Шаг не сдан"),
        ("OK", "Шаг пройден"),
    ]
    status = models.CharField(
        verbose_name="Статус",
        max_length=2,
        choices=STATUS_CHOICES,
        default="PR",
    )

    class Meta:
        verbose_name = "Шаг -> Пользователь [Сайт]"
        verbose_name_plural = "6. Шаги -> Пользователи [Сайт]"
        ordering = ["pk"]
        unique_together = (
            "step",
            "user",
        )
        db_table = "user_step_enrolls"
