from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.products, name='products'),
    path("club/", views.club, name='club'),
    # re_path(r'^products/', views.products),
    # re_path(r'^club/', views.club),
]