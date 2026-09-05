from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('tentang/', views.tentang, name='tentang'),
    path('pengumuman/', views.pengumuman_list, name='pengumuman_list'),
    path('pengumuman/<int:id>/', views.pengumuman_detail, name='pengumuman_detail'),
    path('kontak/', views.kontak, name='kontak'),
]
