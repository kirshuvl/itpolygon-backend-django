from django.urls import path

from core.apps.courses.lms.views import (
    CourseRetrieveAPIView,
)

urlpatterns = [
    path(
        "courses/<int:courseId>/curriculum/",
        CourseRetrieveAPIView.as_view(),
    ),
]
