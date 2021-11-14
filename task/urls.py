
from django.urls import path
from .views import home, clients
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    path('Clients_List', clients, name='clients-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)