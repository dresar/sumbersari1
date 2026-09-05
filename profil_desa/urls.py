from django.urls import path
from . import views

app_name = 'profil_desa'
urlpatterns = [
    path('', views.profil_desa, name='profil'),
]
