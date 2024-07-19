from django.urls import path
from .views import index, products, club

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products'),
    path('club/', club, name='club'),
]