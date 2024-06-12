from django.urls import include, path

urlpatterns = [
    path(
        "",
        include("core.api.lms.dashboard"),
    ),
    path(
        "",
        include("core.api.lms.courses"),
    ),
    path(
        "",
        include("core.api.lms.seminars"),
    ),
    path(
        "",
        include("core.api.lms.homeworks"),
    ),
    path(
        "",
        include("core.api.lms.steps"),
    ),
]
