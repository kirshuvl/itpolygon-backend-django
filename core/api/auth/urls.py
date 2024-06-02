from django.urls import path

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


@extend_schema_view(
    post=extend_schema(
        tags=["AUTH"],
        summary="Obtain a new token pair",
    )
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=["AUTH"],
        summary="Refresh an existing token",
    )
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=["AUTH"],
        summary="Verify an existing token",
    )
)
class CustomTokenVerifyView(TokenVerifyView):
    pass


urlpatterns = [
    path(
        "token/get/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/verify/",
        CustomTokenVerifyView.as_view(),
        name="token_verify",
    ),
    path(
        "token/refresh/",
        CustomTokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
