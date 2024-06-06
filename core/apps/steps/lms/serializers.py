from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from core.apps.steps.models import Step, UserStepEnroll

from rest_framework.serializers import ModelSerializer


class UserStepEnrollCreateSerializer(ModelSerializer):

    class Meta:
        model = UserStepEnroll
        fields = ("step",)


class UserStepEnrollRetrieveSerializer(ModelSerializer):
    class Meta:
        model = UserStepEnroll
        fields = (
            "id",
            "user",
            "step",
            "status",
        )
