from core.apps.courses.serializers import CourseCommonSerializer
from core.apps.seminars.models import Seminar
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.apps.users.serializers import CustomUserCommonSerializer


class SeminarsListSerializer(ModelSerializer):
    teacher = CustomUserCommonSerializer()
    course = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teacher",
            "course",
        )

    def get_course(self, seminar):
        course = seminar.user_seminar_enrolls.first().collection.course

        return CourseCommonSerializer(course, context=self.context).data
