from django.urls import path

from core.apps.seminars.lms.views import SeminarListAPIView

urlpatterns = [
    path(
        "seminars/<int:seminarId>/steps/",
        SeminarListAPIView.as_view(),
    ),
]
