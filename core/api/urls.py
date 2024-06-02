from django.urls import include, path

urlpatterns = [
    path(
        "auth/",
        include(
            "core.api.auth.urls",
        ),
    ),
    path(
        "lms/",
        include(
            "core.api.lms.urls",
        ),
    ),
]
