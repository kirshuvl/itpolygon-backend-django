from django.urls import path

from core.apps.steps.lms.views import (
    UserStepEnrollCreateAPIView,
    UserStepEnrollsUpdateAPIVIew,
)

urlpatterns = [
    path(
        "steps/enrolls/",
        UserStepEnrollCreateAPIView.as_view(),
    ),
    path(
        "steps/enrolls/<int:enrollId>/",
        UserStepEnrollsUpdateAPIVIew.as_view(),
    ),
]
