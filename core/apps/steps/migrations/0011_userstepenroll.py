# Generated by Django 5.0.6 on 2024-06-16 14:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("steps", "0010_useranswerfortestforproblemstep"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserStepEnroll",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("PR", "Шаг изучается"),
                            ("RP", "Шаг повторяется"),
                            ("WA", "Шаг не сдан"),
                            ("OK", "Шаг пройден"),
                            ("WT", "Шаг на проверке"),
                        ],
                        default="PR",
                        max_length=2,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_step_enrolls",
                        to="steps.step",
                        verbose_name="Шаг",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_step_enrolls",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Шаг -> Пользователь [Сайт]",
                "verbose_name_plural": "6. Шаги -> Пользователи [Сайт]",
                "db_table": "user_step_enrolls",
                "ordering": ["pk"],
                "unique_together": {("step", "user")},
            },
        ),
    ]
