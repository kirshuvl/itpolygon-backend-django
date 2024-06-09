from core.apps.courses.models import Course, Lesson, Topic
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

    def get_userEnroll(self, step):
        queryset = step.user_step_enrolls.first()
        if queryset:
            return UserStepEnrollSerializer(queryset).data
        return None

    def get_stepType(self, step: Step):
        return step.get_type()


class TextStepSerializer(ModelSerializer):
    class Meta:
        model = TextStep
        fields = ("id", "text")


class VideoStepSerializer(ModelSerializer):
    class Meta:
        model = VideoStep
        fields = ("id", "video_url")


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


class QuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerForQuestionStep
        fields = "__all__"


class StepSerializer(StepBaseSerializer):
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

    def get_answers(self, step: Step):
        if step.get_type() == "questionstep":
            q = QuestionAnswerSerializer(step.question_answers.all(), many=True)
            print(q, q.data)
            return q.data
        return None


class LessonSerializer(ModelSerializer):
    steps = SerializerMethodField()

    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "number",
            "steps",
        )

    def get_steps(self, lesson):
        queryset = [lesson.step for lesson in lesson.lesson_step_connections.all()]

        return StepSerializer(queryset, many=True).data


class TopicSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Topic
        fields = (
            "id",
            "title",
            "number",
            "lessons",
        )


class CourseSerializer(ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
            "topics",
        )


class CourseListSerializer(ModelSerializer):
    userStatistics = SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
            "userStatistics",
        )

    def get_userStatistics(self, course):

        total_theoretical_steps = 0
        completed_theoretical_steps = 0
        total_practical_steps = 0
        completed_tpractical_steps = 0
        for topic in course.topics.all():
            for lesson in topic.lessons.all():
                for connection in lesson.lesson_step_connections.all():
                    step = connection.step
                    step_type = step.get_type()
                    user_enroll = step.user_step_enrolls.first()
                    if step_type == "textstep" or step_type == "videostep":
                        total_theoretical_steps += 1
                        if user_enroll and user_enroll.status == "OK":
                            completed_theoretical_steps += 1
                    else:
                        total_practical_steps += 1
                        if user_enroll and user_enroll.status == "OK":
                            completed_tpractical_steps += 1
        total_steps = total_theoretical_steps + total_practical_steps
        completed_steps = completed_theoretical_steps + completed_tpractical_steps
        return {
            "totalSteps": total_steps,
            "completedSteps": completed_steps,
            "theoreticalSteps": {
                "total": total_theoretical_steps,
                "completed": completed_theoretical_steps,
            },
            "practicalSteps": {
                "total": total_practical_steps,
                "completed": completed_tpractical_steps,
            },
        }
