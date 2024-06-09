from django.urls import path

from core.apps.homeworks.lms.views import (
    HomeworkListAPIView,
    HomeworkRetrieveAPIView,
    CourseHomeworkListAPIView,
)

urlpatterns = [
    path(
        "homeworks/",
        HomeworkListAPIView.as_view(),
    ),
    path(
        "homeworks/<int:homeworkId>/",
        HomeworkRetrieveAPIView.as_view(),
    ),
    path(
        "courses/<int:courseId>/homeworks/",
        CourseHomeworkListAPIView.as_view(),
    ),
]
