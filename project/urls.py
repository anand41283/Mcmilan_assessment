"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('v2/student',StudentView,basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('super/register/',UserRegistrationView.as_view(),name="s_reg"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_for_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('Add/dept/', Adddept.as_view(), name='A_dept'),

]+router.urls
