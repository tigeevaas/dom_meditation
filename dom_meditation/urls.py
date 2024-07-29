from django.contrib import admin
from django.urls import path, include, re_path
from main import views

from dom_meditation import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path('admin/', admin.site.urls),
    path("products/", views.products, name='products'),
    path("club/", views.club, name='club'),
    path("practicums/", views.practicums, name='practicums'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if settings.DEBUG else []



