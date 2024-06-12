from django.urls import include, path

urlpatterns = [
    path(
        "",
        include("core.api.lms.dashboard"),
    ),
]
