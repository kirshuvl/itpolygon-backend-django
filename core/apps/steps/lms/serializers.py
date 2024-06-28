from core.apps.steps.models import (
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserStepBookmark,
    UserStepEnroll,
    UserStepLike,
    UserStepView,
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


class UserStepLikeSerializer(ModelSerializer):
    class Meta:
        model = UserStepLike
        fields = (
            "id",
            "user",
            "step",
            "source",
        )


class UserStepBookmarkSerializer(ModelSerializer):
    class Meta:
        model = UserStepBookmark
        fields = (
            "id",
            "user",
            "step",
            "source",
        )


class UserStepViewSerializer(ModelSerializer):
    class Meta:
        model = UserStepView
        fields = (
            "id",
            "user",
            "step",
            "source",
        )
