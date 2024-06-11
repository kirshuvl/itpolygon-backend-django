from core.apps.homeworks.models import Homework
from core.apps.seminars.models import Seminar

from core.apps.courses.lms.serializers import StepSerializer
from core.apps.users.serializers import CustomUserCommonSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class SeminarRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Seminar
        fields = (
            "id",
            "date",
        )


class HomeworkSerializer(ModelSerializer):
    author = CustomUserCommonSerializer()
    seminar = SeminarRetrieveSerializer()
    steps = SerializerMethodField()

    class Meta:
        model = Homework
        fields = (
            "id",
            "author",
            "seminar",
            "steps",
            "course",
        )

    def get_steps(self, seminar):
        connections = seminar.homework_step_connections.all()
        steps = [connection.step for connection in connections]
        return StepSerializer(steps, many=True).data
