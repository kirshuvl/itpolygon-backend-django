from core.apps.courses.models import Course

from rest_framework.serializers import ModelSerializer, SerializerMethodField


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
