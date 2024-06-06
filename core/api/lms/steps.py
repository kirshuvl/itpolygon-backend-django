from django.urls import path

from core.apps.steps.lms.views import UserStepEnrollCreateAPIView

urlpatterns = [
    path(
        "steps/enrolls/",
        UserStepEnrollCreateAPIView.as_view(),
    ),
]
