from django.urls import path

from core.apps.homeworks.lms.views import HomeworksListAPIView

urlpatterns = [
    path(
        "homeworks/",
        HomeworksListAPIView.as_view(),
    )
]
