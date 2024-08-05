from core.apps.steps.models import (
    AnswerForSingleChoiceQuestionStep,
    ProblemStep,
    QuestionStep,
    SingleChoiceQuestionStep,
    Step,
    TestForProblemStep,
    TextStep,
    UserAnswerForProblemStep,
    UserAnswerForQuestionStep,
    UserAnswerForSingleChoiceQuestionStep,
    UserStepEnroll,
    UserStepLike,
    VideoStep,
)

from rest_framework.serializers import IntegerField, ModelSerializer, SerializerMethodField


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
    userLike = SerializerMethodField()

    class Meta:
        model = Step
        fields = (
            "id",
            "title",
            "stepType",
            "liked_by",
            "bookmarked_by",
            "viewed_by",
            "userEnroll",
            "userLike",
        )

    def get_stepType(self, step: Step):
        return step.get_type()

    def get_userEnroll(self, step):
        queryset = step.user_step_enrolls.first()
        if queryset:
            return UserStepEnrollSerializer(queryset).data
        return None

    def get_userLike(self, step):
        queryset = step.user_step_likes.first()

        if queryset:
            return UserStepLikeCommonSerializer(queryset).data
        return None


class UserStepLikeCommonSerializer(ModelSerializer):
    class Meta:
        model = UserStepLike
        fields = ("id",)


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


class SingleChoiceQuestionStepSerializer(ModelSerializer):
    stepAnswers = SerializerMethodField()
    userAnswers = SerializerMethodField()

    class Meta:
        model = SingleChoiceQuestionStep
        fields = (
            "id",
            "text",
            "stepAnswers",
            "userAnswers",
        )

    def get_stepAnswers(self, step):
        step_answers = step.answer_for_single_choice_question_steps.all()
        return AnswerForSingleChoiceQuestionStepSerializer(
            step_answers,
            context=self.context,
            many=True,
        ).data

    def get_userAnswers(self, step):
        user_answers = step.user_answer_for_single_choice_question_steps.all()
        return UserAnswerForSingleChoiceQuestionStepSerializer(
            user_answers,
            context=self.context,
            many=True,
        ).data


class AnswerForSingleChoiceQuestionStepSerializer(ModelSerializer):
    class Meta:
        model = AnswerForSingleChoiceQuestionStep
        fields = (
            "id",
            "answer",
            "is_correct",
        )


class ProblemStepSerializer(ModelSerializer):
    userAnswers = SerializerMethodField()
    stepTests = SerializerMethodField()
    cpuTime = IntegerField(source="cpu_time")

    class Meta:
        model = ProblemStep
        fields = (
            "id",
            "text",
            "input",
            "output",
            "notes",
            "cpuTime",
            "memory",
            "userAnswers",
            "stepTests",
        )

    def get_userAnswers(self, step: ProblemStep):
        user_answers = step.user_answer_for_problem_steps.all()
        return UserAnswerForProblemStepCommonSerializer(
            user_answers,
            context=self.context,
            many=True,
        ).data

    def get_stepTests(self, step: ProblemStep):
        step_tests = [
            test
            for test in step.tests.all()
            if test.number >= step.first_sample and test.number <= step.last_sample
        ]

        return TestForProblemStepSerializer(
            step_tests,
            many=True,
        ).data


class TestForProblemStepSerializer(ModelSerializer):
    class Meta:
        model = TestForProblemStep
        fields = (
            "id",
            "number",
            "input",
            "output",
        )


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
        elif step_type == "singlechoicequestionstep":
            return SingleChoiceQuestionStepSerializer(step.singlechoicequestionstep).data


class UserAnswerForQuestionStepCommonSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForQuestionStep
        fields = (
            "id",
            "answer",
            "is_correct",
            "created_at",
        )


class AnswerForSingleChoiceQuestionStepRetrieveSerializer(ModelSerializer):
    class Meta:
        model = AnswerForSingleChoiceQuestionStep
        fields = (
            "id",
            "answer",
            "is_correct",
        )


class UserAnswerForSingleChoiceQuestionStepSerializer(ModelSerializer):
    answer = AnswerForSingleChoiceQuestionStepRetrieveSerializer()

    class Meta:
        model = UserAnswerForSingleChoiceQuestionStep
        fields = (
            "id",
            "answer",
            "created_at",
        )


class UserAnswerForProblemStepCommonSerializer(ModelSerializer):
    cpuTime = IntegerField(source="cpu_time")

    class Meta:
        model = UserAnswerForProblemStep
        fields = (
            "id",
            "language",
            "verdict",
            "cpuTime",
            "created_at",
        )
