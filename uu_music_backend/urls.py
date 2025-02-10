"""
URL configuration for uu_music_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse


def test(request):
    name=request.GET.get("pwd",'Defaltname')
    print(name)
    print(request)
    return HttpResponse("<h1>test</h1>")


urlpatterns = [
    path("login/",include("login.urls")),
    path("test/",test)
]
