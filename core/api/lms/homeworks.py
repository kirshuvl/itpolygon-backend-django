from django.urls import path

from core.apps.collections.lms.views import (
    CourseHomeworkListAPIView,
    HomeworkListAPIView,
    HomeworkRetrieveAPIView,
)

urlpatterns = [
    path(
        "homeworks/",
        HomeworkListAPIView.as_view(),
    ),
    path(
        "homeworks/<int:homeworkId>/steps/",
        HomeworkRetrieveAPIView.as_view(),
    ),
    path(
        "courses/<int:courseId>/homeworks/",
        CourseHomeworkListAPIView.as_view(),
    ),
]
