from django.urls import path
from . import views

app_name = 'berita'
urlpatterns = [
    path('', views.berita_list, name='list'),
    path('<slug:slug>/', views.berita_detail, name='detail'),
]
