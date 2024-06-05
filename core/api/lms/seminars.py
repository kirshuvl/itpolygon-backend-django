from django.urls import path

from core.apps.seminars.lms.views import SeminarsListAPIView

urlpatterns = [
    path(
        "seminars/",
        SeminarsListAPIView.as_view(),
    )
]
