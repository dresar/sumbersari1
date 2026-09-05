from django.contrib import admin
from .models import Galeri

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ['judul', 'tipe', 'tanggal', 'aktif']
    list_filter = ['tipe', 'aktif', 'tanggal']
    search_fields = ['judul', 'deskripsi']
