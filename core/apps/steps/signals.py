from django.db import models, transaction
from django.dispatch import receiver

from core.apps.steps.models import Step, UserStepBookmark, UserStepLike, UserStepView
from django.db.models.signals import post_delete, post_save


@receiver(post_save, sender=UserStepLike)
def create_user_step_like(sender, instance: UserStepLike, created, **kwargs):
    if created:
        step: Step = instance.step
        with transaction.atomic():
            step.liked_by = models.F("liked_by") + 1
            step.save()


@receiver(post_delete, sender=UserStepLike)
def delete_user_step_like(sender, instance: UserStepLike, **kwargs):
    step: Step = instance.step
    with transaction.atomic():
        if step.liked_by > 0:
            step.liked_by = models.F("liked_by") - 1
            step.save()


@receiver(post_save, sender=UserStepBookmark)
def create_user_step_bookmark(sender, instance: UserStepBookmark, created, **kwargs):
    if created:
        step: Step = instance.step
        with transaction.atomic():
            step.bookmarked_by = models.F("bookmarked_by") + 1
            step.save()


@receiver(post_delete, sender=UserStepBookmark)
def delete_user_step_bookmark(sender, instance: UserStepBookmark, **kwargs):
    step: Step = instance.step
    with transaction.atomic():
        if step.bookmarked_by > 0:
            step.bookmarked_by = models.F("bookmarked_by") - 1
            step.save()


@receiver(post_save, sender=UserStepView)
def create_user_step_view(sender, instance: UserStepView, created, **kwargs):
    if created:
        step: Step = instance.step
        with transaction.atomic():
            step.viewed_by = models.F("viewed_by") + 1
            step.save()


@receiver(post_delete, sender=UserStepView)
def delete_user_step_view(sender, instance: UserStepView, **kwargs):
    step: Step = instance.step
    with transaction.atomic():
        if step.viewed_by > 0:
            step.viewed_by = models.F("viewed_by") - 1
            step.save()
