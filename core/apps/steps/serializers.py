from core.apps.steps.models import (
    ProblemStep,
    QuestionStep,
    Step,
    TextStep,
    UserAnswerForQuestionStep,
    UserStepEnroll,
    VideoStep,
)

from rest_framework.serializers import ModelSerializer, SerializerMethodField


class UserStepEnrollSerializer(ModelSerializer):
    class Meta:
        model = UserStepEnroll
        fields = (
            "id",
            "status",
        )


class StepBaseSerializer(ModelSerializer):
    stepType = SerializerMethodField()
    userEnroll = SerializerMethodField()

    class Meta:
        model = Step
        fields = (
            "id",
            "title",
            "stepType",
            "userEnroll",
        )

    def get_stepType(self, step: Step):
        return step.get_type()

    def get_userEnroll(self, step):
        queryset = step.user_step_enrolls.first()
        if queryset:
            return UserStepEnrollSerializer(queryset).data
        return None


class TextStepSerializer(ModelSerializer):
    class Meta:
        model = TextStep
        fields = (
            "id",
            "text",
        )


class VideoStepSerializer(ModelSerializer):
    class Meta:
        model = VideoStep
        fields = (
            "id",
            "video_url",
        )


class QuestionStepSerializer(ModelSerializer):
    class Meta:
        model = QuestionStep
        fields = (
            "id",
            "text",
        )


class ProblemStepSerializer(ModelSerializer):
    class Meta:
        model = ProblemStep
        fields = (
            "id",
            "text",
            "input",
            "output",
            "notes",
        )


class StepRetrieveSerializer(StepBaseSerializer):
    body = SerializerMethodField()
    userAnswers = SerializerMethodField()

    class Meta:
        model = Step
        fields = StepBaseSerializer.Meta.fields + (
            "body",
            "userAnswers",
        )

    def get_body(self, step: Step):
        step_type = step.get_type()
        if step_type == "textstep":
            return TextStepSerializer(step.textstep).data
        elif step_type == "videostep":
            return VideoStepSerializer(step.videostep).data
        elif step_type == "questionstep":
            return QuestionStepSerializer(step.questionstep).data
        elif step_type == "problemstep":
            return ProblemStepSerializer(step.problemstep).data

    def get_userAnswers(self, step: Step):
        step_type = step.get_type()
        if step_type == "questionstep":
            user_answers = step.question_answers.all()
            return UserAnswerForQuestionStepCommonSerializer(
                user_answers, context=self.context, many=True
            ).data
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.get_type() != "questionstep":
            representation.pop("userAnswers", None)
        return representation


class UserAnswerForQuestionStepCommonSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForQuestionStep
        fields = (
            "id",
            "user",
            "question",
            "answer",
            "is_correct",
        )
