from django.urls import include, path

urlpatterns = [
    path(
        "",
        include("core.api.lms.courses"),
    ),
    path(
        "",
        include("core.api.lms.seminars"),
    ),
]
