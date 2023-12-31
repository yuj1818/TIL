from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("music.urls")),
    path("api/v1/", SpectacularAPIView.as_view(), name='schema'),
    path("api/v1/swagger/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/v1/redocs/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
