from django.urls import path

from core.apps.seminars.lms.views import SeminarRetrieveAPIView

urlpatterns = [
    path(
        "seminars/<int:seminarId>/steps/",
        SeminarRetrieveAPIView.as_view(),
    ),
]
