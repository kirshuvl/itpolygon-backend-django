from django.urls import path

from core.apps.collections.lms.views import HomeworkListAPIView
from core.apps.courses.lms.views import CourseListAPIView
from core.apps.seminars.lms.views import SeminarListAPIView

urlpatterns = [
    path(
        "courses/",
        CourseListAPIView.as_view(),
    ),
    path(
        "homeworks/",
        HomeworkListAPIView.as_view(),
    ),
    path(
        "seminars/",
        SeminarListAPIView.as_view(),
    ),
]
