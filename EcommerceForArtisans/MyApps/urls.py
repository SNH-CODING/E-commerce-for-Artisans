import imp
from django.urls import path
from . import views


# URLS
urlpatterns = [
    path('', views.index, name="index"),
]
