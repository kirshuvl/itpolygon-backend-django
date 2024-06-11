from django.urls import path

from core.apps.courses.lms.views import (
    CourseListAPIView,
    CourseRetrieveAPIView,
    LessonRetrieveAPIView,
)

urlpatterns = []
"""
path(
        "courses/<int:courseId>/curriculum/",
        CourseRetrieveAPIView.as_view(),
    ),
    path(
        "lessons/<int:lessonId>/steps/",
        LessonRetrieveAPIView.as_view(),
    ),

"""
