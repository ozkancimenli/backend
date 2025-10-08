from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# -----------------------------------------------------------------------------
# Swagger Schema Configuration
# -----------------------------------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="TaskTrackr Pro API",
        default_version='v1',
        description="Fullstack Task Management API with JWT Auth, Projects & Tasks",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@tasktrackrpro.dev"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path('api/users/', include('users.urls')),
        path('api/projects/', include('projects.urls')),
        path('api/tasks/', include('tasks.urls')),
    ],
)

# -----------------------------------------------------------------------------
# URL Patterns
# -----------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),

    # Swagger & Redoc routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# -----------------------------------------------------------------------------
# Static Files (Swagger UI + Admin + DRF)
# -----------------------------------------------------------------------------
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
