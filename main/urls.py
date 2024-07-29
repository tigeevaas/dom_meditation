from django.urls import path, re_path
from .views import index, products, club, practicums
from . import views

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products'),
    path('club/', club, name='club'),
    path('practicums/', practicums, name='practicums')
]