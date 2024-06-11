from rest_framework.serializers import ModelSerializer

from core.apps.courses.models import Course


class CourseCommonSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
        )
