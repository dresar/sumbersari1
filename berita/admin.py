from django.contrib import admin
from .models import KategoriBerita, Berita

@admin.register(KategoriBerita)
class KategoriBeritaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'slug']
    prepopulated_fields = {'slug': ('nama',)}

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['judul', 'kategori', 'penulis', 'tanggal_publish', 'aktif']
    list_filter = ['kategori', 'aktif', 'tanggal_publish']
    search_fields = ['judul', 'konten']
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'tanggal_publish'
