from core.apps.courses.models import Course
from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser

from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField


class TeacherRetrieveSerializer(ModelSerializer):
    firstName = CharField(source="first_name")
    lastName = CharField(source="last_name")

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "firstName",
            "lastName",
        )


class CourseSerializer(ModelSerializer):

    icon = SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
        )

    def get_icon(self, instance):
        if instance.icon and instance.icon.url:
            return self.context["request"].build_absolute_uri(instance.icon.url)
        return None


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
        return CourseSerializer(courses, context={"request": self.context["request"]}).data


class SeminarsRetrieveSerializer(ModelSerializer):
    teachers = SerializerMethodField()

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
