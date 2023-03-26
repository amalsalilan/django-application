"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views

"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def myfirstwebpage(request):
    return HttpResponse("hello this is my first webpage")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Hello",myfirstwebpage)
]
