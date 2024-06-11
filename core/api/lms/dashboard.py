from django.urls import path

from core.apps.courses.lms.views import CourseListAPIView

urlpatterns = [
    path(
        "courses/",
        CourseListAPIView.as_view(),
    ),
]
