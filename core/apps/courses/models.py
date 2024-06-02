from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.steps.models import Step
from core.apps.users.models import CustomUser


class Course(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название курса",
        max_length=255,
        unique=True,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    icon = models.ImageField(
        verbose_name="Иконка курса",
        upload_to="icon/course/",
        blank=True,
    )

    description = models.TextField(
        verbose_name="Описание курса",
        blank=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "1. Курсы"
        ordering = ["pk"]
        db_table = "courses"

    def __str__(self) -> str:
        return self.title


class Topic(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название темы",
        max_length=50,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    course = models.ForeignKey(
        Course,
        related_name="topics",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ темы в курсе",
        default=1000,
    )

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "2. Темы"
        ordering = ["pk"]
        unique_together = (
            "course",
            "number",
        )
        db_table = "topics"

    def __str__(self) -> str:
        return f"{self.title}"


class Lesson(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название урока",
        max_length=50,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать",
        default=True,
    )

    topic = models.ForeignKey(
        Topic,
        related_name="lessons",
        verbose_name="Тема",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ урока в теме",
        default=1000,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "3. Уроки"
        ordering = ["pk"]
        unique_together = (
            "topic",
            "number",
        )
        db_table = "lessons"

    def __str__(self) -> str:
        return f"{self.title}"


class AuthorCourseEnroll(TimedBaseModel):
    author = models.ForeignKey(
        CustomUser,
        related_name="author_course_enrolls",
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        related_name="author_course_enrolls",
        verbose_name="Курс",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Курс -> Автор"
        verbose_name_plural = "5. Курсы -> Авторы"
        ordering = ["pk"]
        unique_together = (
            "author",
            "course",
        )
        db_table = "author_course_enrolls"

    def __str__(self) -> str:
        return f"{self.course} -> {self.user}"


class LessonStepConnection(TimedBaseModel):
    lesson = models.ForeignKey(
        Lesson,
        related_name="lesson_step_connections",
        verbose_name="Урок",
        on_delete=models.CASCADE,
    )

    step = models.ForeignKey(
        Step,
        related_name="lesson_step_connections",
        verbose_name="Шаг",
        on_delete=models.CASCADE,
    )

    number = models.IntegerField(
        verbose_name="№ шага в уроке",
        default=1000,
    )

    is_published = models.BooleanField(
        verbose_name="Опубликовать?",
        default=False,
    )

    class Meta:
        verbose_name = "Уроки -> Шаг"
        verbose_name_plural = "4. Уроки -> Шаги"
        ordering = ["pk"]
        db_table = "lesson_step_connections"
        unique_together = (
            "lesson",
            "step",
        )


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

    class Meta:
        verbose_name = "Курс -> Студент"
        verbose_name_plural = "5. Курсы -> Студенты"
        ordering = ("pk",)
        unique_together = (
            "user",
            "course",
        )
        db_table = "user_course_enrolls"

    def __str__(self) -> str:
        return f"{self.course} -> {self.user}"
