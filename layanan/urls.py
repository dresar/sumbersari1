from django.urls import path
from . import views

app_name = 'layanan'
urlpatterns = [
    path('', views.layanan_list, name='list'),
    path('<int:id>/', views.layanan_detail, name='detail'),
]
