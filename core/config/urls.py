from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "__debug__/",
        include("debug_toolbar.urls"),
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "",
            include("core.api.urls"),
        ),
        path(
            "schema/",
            SpectacularAPIView.as_view(),
            name="schema",
        ),
        path(
            "schema/swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger",
        ),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
