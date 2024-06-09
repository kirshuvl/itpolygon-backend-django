from core.apps.courses.models import Course
from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser

from core.apps.courses.lms.serializers import StepSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class TeacherRetrieveSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "icon",
        )


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
        )


class SeminarsListSerializer(ModelSerializer):
    teachers = SerializerMethodField()
    course = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teachers",
            "course",
        )

    def get_teachers(self, seminar):
        enrolls = seminar.teacher_seminar_enrolls.all()
        teachers = [enroll.teacher for enroll in enrolls]
        if teachers:
            return TeacherRetrieveSerializer(teachers, many=True).data
        return None

    def get_course(self, seminar):
        q = seminar.user_seminar_enrolls.all()
        courses = [enroll.course for enroll in q][0]
        return CourseSerializer(courses).data


class SeminarsRetrieveSerializer(ModelSerializer):
    teachers = SerializerMethodField()
    steps = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "steps",
            "teachers",
        )

    def get_teachers(self, seminar):
        enrolls = seminar.teacher_seminar_enrolls.all()
        teachers = [enroll.teacher for enroll in enrolls]
        if teachers:
            return TeacherRetrieveSerializer(teachers, many=True).data
        return None

    def get_steps(self, seminar):
        connections = seminar.seminar_step_connections.all()
        steps = [connection.step for connection in connections]
        return StepSerializer(steps, many=True).data
