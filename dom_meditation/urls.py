from django.contrib import admin
from django.urls import path, include  # new
from main import views

urlpatterns = [
    path("", views.index),
    path("products/", views.products),
]