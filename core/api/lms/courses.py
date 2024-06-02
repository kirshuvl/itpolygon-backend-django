from django.urls import path

from core.apps.courses.lms.views import CoursesListAPIView

urlpatterns = [
    path(
        "courses/",
        CoursesListAPIView.as_view(),
    ),
]
