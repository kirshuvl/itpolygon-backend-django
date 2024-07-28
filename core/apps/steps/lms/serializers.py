from core.apps.steps.models import (
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserAnswerForSingleChoiceQuestionStep,
    UserStepBookmark,
    UserStepEnroll,
    UserStepLike,
    UserStepView,
    AnswerForSingleChoiceQuestionStep,
)

from rest_framework.serializers import ModelSerializer

from core.apps.steps.serializers import AnswerForSingleChoiceQuestionStepRetrieveSerializer


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


class UserAnswerForSingleChoiceQuestionStepCreateSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForSingleChoiceQuestionStep
        fields = (
            "id",
            "question",
            "answer",
        )


class UserAnswerForSingleChoiceQuestionStepRetrieveSerializer(ModelSerializer):
    answer = AnswerForSingleChoiceQuestionStepRetrieveSerializer()

    class Meta:
        model = UserAnswerForSingleChoiceQuestionStep
        fields = (
            "id",
            "answer",
            "created_at",
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
            "step",
            "source",
        )
