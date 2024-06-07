from django.urls import path

from core.apps.seminars.lms.views import SeminarListAPIView, SeminarRetrieveAPIView

urlpatterns = [
    path(
        "seminars/",
        SeminarListAPIView.as_view(),
    ),
    path(
        "seminars/<int:seminarId>/",
        SeminarRetrieveAPIView.as_view(),
    ),
]
