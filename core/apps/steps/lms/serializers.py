from core.apps.steps.models import (
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserStepEnroll,
)

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
            "status",
        )


class UserAnswerForQuestionStepCreateSerializer(ModelSerializer):

    class Meta:
        model = UserAnswerForQuestionStep
        fields = (
            "id",
            "question",
            "answer",
            "is_correct",
        )


class UserAnswerForProblemStepCreateSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForProblemStep
        fields = (
            "id",
            "code",
            "problem",
        )
