# Generated by Django 5.0.6 on 2024-06-16 14:09

from django.conf import settings
from django.db import migrations, models

import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("collections", "0002_collectionstepconnection"),
        ("dashboard", "0001_usercourseenroll"),
        ("seminars", "0001_seminar"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserHomeworkEnroll",
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
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_homework_enrolls",
                        to="collections.collection",
                        verbose_name="Коллекция заданий",
                    ),
                ),
                (
                    "seminar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_homework_enrolls",
                        to="seminars.seminar",
                        verbose_name="Семинар",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_homework_enrolls",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Студент -> Домашнее задание",
                "verbose_name_plural": "3. Студенты -> Домашнее задание",
                "db_table": "user_homework_enrolls",
                "ordering": ("pk",),
                "unique_together": {("user", "seminar")},
            },
        ),
    ]
