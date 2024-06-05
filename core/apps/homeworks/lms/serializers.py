from core.apps.homeworks.models import Homework
from core.apps.seminars.models import Seminar
from core.apps.users.models import CustomUser

from rest_framework.serializers import ModelSerializer


class TeacherRetrieveSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "icon",
        )


class SeminarRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
        )


class HomeworksListSerializer(ModelSerializer):
    author = TeacherRetrieveSerializer()
    seminar = SeminarRetrieveSerializer()

    class Meta:
        model = Homework
        fields = (
            "id",
            "author",
            "seminar",
        )
