"""ncstools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from ncstools.views import main
from appAPIv1 import views
from appAccounts.views import NCSLoginView


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectViewSet)


urlpatterns = [
    path('', main),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/token/obtain/', obtain_jwt_token),
    path('auth/token/refresh/', refresh_jwt_token),
    path('auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('my-auth/', NCSLoginView.as_view())
]
