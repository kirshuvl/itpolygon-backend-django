# Generated by Django 5.0.6 on 2024-06-16 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("steps", "0009_useranswerforproblemstep"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAnswerForTestForProblemStep",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                (
                    "verdict",
                    models.CharField(
                        choices=[
                            ("PR", "На проверке"),
                            ("OK", "OK"),
                            ("CE", "Ошибка компиляции"),
                            ("WA", "Неправильный ответ"),
                            ("TL", "Превышение времени"),
                            ("ML", "Превышение памяти"),
                            ("UN", "Незвестная ошибка"),
                        ],
                        default="WA",
                        max_length=2,
                        verbose_name="Вердикт",
                    ),
                ),
                ("exit_code", models.IntegerField(verbose_name="exit_code")),
                ("stdout", models.TextField(max_length=10000, verbose_name="stdout")),
                ("stderr", models.TextField(max_length=10000, verbose_name="stderr")),
                ("duration", models.FloatField(default=0, verbose_name="duration")),
                ("timeout", models.BooleanField(default=False, verbose_name="timeout")),
                ("oom_killed", models.BooleanField(default=False, verbose_name="oom_killed")),
                (
                    "code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_answer_for_test_for_problem_steps",
                        to="steps.useranswerforproblemstep",
                        verbose_name="Решение пользователя",
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_answer_for_test_for_problem_steps",
                        to="steps.testforproblemstep",
                        verbose_name="Тест",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_answer_for_test_for_problem_steps",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат теста",
                "verbose_name_plural": "5. Шаги [Программирование][Тесты] -> [Ответ]",
                "ordering": ["pk"],
            },
        ),
    ]
