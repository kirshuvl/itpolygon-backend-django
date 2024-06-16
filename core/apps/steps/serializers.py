from core.apps.steps.models import (
    ProblemStep,
    QuestionStep,
    Step,
    TextStep,
    UserAnswerForProblemStep,
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
    userAnswers = SerializerMethodField()

    class Meta:
        model = QuestionStep
        fields = (
            "id",
            "text",
            "userAnswers",
        )

    def get_userAnswers(self, step):
        user_answers = step.user_answer_for_question_steps.all()
        return UserAnswerForQuestionStepCommonSerializer(
            user_answers, context=self.context, many=True
        ).data


class ProblemStepSerializer(ModelSerializer):
    userProblems = SerializerMethodField()

    class Meta:
        model = ProblemStep
        fields = (
            "id",
            "text",
            "input",
            "output",
            "notes",
            "userProblems",
        )

    def get_userProblems(self, step):
        user_answers = step.codes.all()
        return UserAnswerForProblemStepCommonSerializer(
            user_answers, context=self.context, many=True
        ).data


class StepRetrieveSerializer(StepBaseSerializer):
    body = SerializerMethodField()

    class Meta:
        model = Step
        fields = StepBaseSerializer.Meta.fields + ("body",)

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


class UserAnswerForProblemStepCommonSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForProblemStep
        fields = (
            "id",
            "language",
            "verdict",
            "cputime",
        )
