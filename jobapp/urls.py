"""
URL configuration for jobapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path("signup/",signuppage,name="signup"),
    path('login/',loginview,name='login'),
    path('logout/',logout,name="logout"),
    path("jobdetails/<int:id>/",jobdetails,name="jobdetails"),
    path("userprofile/",userdashboard,name="userprofile"),
    path('addjob/',add_job,name='addjob'),
    path('applyjob/<int:id>/',applyjob,name='applyjob'),
    path('view_application/<int:application_id>/',view_applicantion, name='view_application'),
]
