from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Memno image",
        default_version="v1",
        description="memno сайт для просмотра мемов",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("", include("src.user.urls")),
    path("image/", include("src.image_library.urls")),
    # path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
