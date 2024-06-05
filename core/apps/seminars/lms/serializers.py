from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser

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


class SeminarsListSerializer(ModelSerializer):
    teachers = SerializerMethodField()

    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
            "teachers",
        )

    def get_teachers(self, seminar):
        queryset = seminar.teacher_seminar_enrolls.all()
        teachers = [enroll.teacher for enroll in queryset]
        print(teachers)
        if queryset:
            return TeacherRetrieveSerializer(teachers, many=True).data
        return None
