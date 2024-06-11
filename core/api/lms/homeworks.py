from django.urls import path

from core.apps.seminars.lms.views import HomeworkRetrieveAPIView

urlpatterns = [
    path(
        "homeworks/<int:homeworkId>/steps/",
        HomeworkRetrieveAPIView.as_view(),
    ),
]
