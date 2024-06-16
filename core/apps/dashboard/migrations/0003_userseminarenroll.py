# Generated by Django 5.0.6 on 2024-06-16 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collections", "0002_collectionstepconnection"),
        ("dashboard", "0002_userhomeworkenroll"),
        ("seminars", "0001_seminar"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSeminarEnroll",
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
                        blank=True,
                        choices=[
                            ("WAS", "Был"),
                            ("WASNT", "Не был"),
                            ("SICK", "Болел"),
                            ("NCH", "Не выбрано"),
                        ],
                        default="NCH",
                        max_length=7,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_seminar_enrolls",
                        to="collections.collection",
                        verbose_name="Коллекция заданий",
                    ),
                ),
                (
                    "seminar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_seminar_enrolls",
                        to="seminars.seminar",
                        verbose_name="Семинар",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_seminar_enrolls",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Студент -> Семинар",
                "verbose_name_plural": "2. Студенты -> Семинары",
                "db_table": "user_seminar_enrolls",
                "ordering": ("pk",),
                "unique_together": {("user", "seminar")},
            },
        ),
    ]
