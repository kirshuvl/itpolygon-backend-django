from core.apps.courses.models import Course

from rest_framework.serializers import ModelSerializer


class CourseCommonSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "icon",
        )
