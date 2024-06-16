from core.apps.seminars.models import Seminar

from core.apps.courses.serializers import CourseCommonSerializer
from core.apps.steps.serializers import StepRetrieveSerializer
from core.apps.users.serializers import CustomUserCommonSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class SeminarsListSerializer(ModelSerializer):
    teacher = CustomUserCommonSerializer()
    course = SerializerMethodField()
    userStatistics = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teacher",
            "course",
            "userStatistics",
        )

    def get_course(self, seminar):
        course = seminar.user_seminar_enrolls.first().collection.course

        return CourseCommonSerializer(course, context=self.context).data

    def get_userStatistics(self, seminar):

        total_theoretical_steps = 0
        completed_theoretical_steps = 0
        total_practical_steps = 0
        completed_tpractical_steps = 0
        connections = (
            seminar.user_seminar_enrolls.first().collection.collection_step_connections.all()
        )
        steps = [connection.step for connection in connections]

        for step in steps:
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


class HomeworkListSerializer(ModelSerializer):
    teacher = CustomUserCommonSerializer()
    course = SerializerMethodField()
    userStatistics = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teacher",
            "course",
            "userStatistics",
        )

    def get_course(self, seminar):
        course = seminar.user_homework_enrolls.first().collection.course

        return CourseCommonSerializer(course, context=self.context).data

    def get_userStatistics(self, seminar):

        total_theoretical_steps = 0
        completed_theoretical_steps = 0
        total_practical_steps = 0
        completed_tpractical_steps = 0
        connections = (
            seminar.user_homework_enrolls.first().collection.collection_step_connections.all()
        )
        steps = [connection.step for connection in connections]

        for step in steps:
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


class SeminarRetrieveSerializer(ModelSerializer):
    teacher = CustomUserCommonSerializer()
    course = SerializerMethodField()
    steps = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teacher",
            "course",
            "steps",
        )

    def get_course(self, seminar):
        course = seminar.user_seminar_enrolls.first().collection.course

        return CourseCommonSerializer(course, context=self.context).data

    def get_steps(self, seminar):
        connections = (
            seminar.user_seminar_enrolls.first().collection.collection_step_connections.all()
        )
        steps = [connection.step for connection in connections]

        return StepRetrieveSerializer(steps, many=True).data


class HomeworkRetrieveSerializer(ModelSerializer):
    teacher = CustomUserCommonSerializer()
    course = SerializerMethodField()
    steps = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teacher",
            "course",
            "steps",
        )

    def get_course(self, seminar):
        course = seminar.user_homework_enrolls.first().collection.course

        return CourseCommonSerializer(course, context=self.context).data

    def get_steps(self, seminar):
        connections = (
            seminar.user_homework_enrolls.first().collection.collection_step_connections.all()
        )
        steps = [connection.step for connection in connections]

        return StepRetrieveSerializer(steps, many=True).data
