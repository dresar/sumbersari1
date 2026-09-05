from django.contrib import admin
from .models import KategoriLayanan, Layanan

@admin.register(KategoriLayanan)
class KategoriLayananAdmin(admin.ModelAdmin):
    list_display = ['nama', 'icon']

@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'waktu_penyelesaian', 'aktif']
    list_filter = ['kategori', 'aktif']
    search_fields = ['nama', 'deskripsi']
