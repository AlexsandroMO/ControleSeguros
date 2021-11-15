
from django.urls import path
from .views import home, clients, CreateDB, Spreadsheet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home-home'),
    path('Clients_List', clients, name='clients-list'),
    path('Spreadsheet_List', Spreadsheet, name='spreadsheet_list'),
    path('Create_DB', CreateDB, name='create-db'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)