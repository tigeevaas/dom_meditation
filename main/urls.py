from django.urls import path, re_path
from .views import index, products, club, practicums, meditations, efiry

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products'),
    path('club/', club, name='club'),
    path('practicums/', practicums, name='practicums'),
    path('meditations/', meditations, name='meditations'),
    path('efiry/', efiry, name='efiry'),
]