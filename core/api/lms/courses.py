from django.urls import path

from core.apps.courses.lms.views import (
    CourseListAPIView,
    CourseRetrieveAPIView,
    LessonRetrieveAPIView,
)

urlpatterns = [
    path(
        "courses/",
        CourseListAPIView.as_view(),
    ),
    path(
        "courses/<int:courseId>/curriculum/",
        CourseRetrieveAPIView.as_view(),
    ),
    path(
        "lessons/<int:lessonId>/",
        LessonRetrieveAPIView.as_view(),
    ),
]
