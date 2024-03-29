"""UniLikes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import permissions, routers
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import voting.views
import teacher.views

schema_view = get_schema_view(
    openapi.Info(
        title="UniLikes API",
        default_version='v1',
        description="Hey, we are UniLikes! Our voting system is free and anonymous!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="easydush@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'voting', voting.views.VotingViewSet, basename='voting')
router.register(r'teacher', teacher.views.TeacherViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path to our account's app endpoints
    # path("api/account/", include("account.urls"))
]
