from django.contrib import admin
from .models import Slider, Pengumuman, ProfilDesa, StatistikDesa

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['judul', 'aktif', 'urutan', 'dibuat']
    list_filter = ['aktif', 'dibuat']
    search_fields = ['judul', 'deskripsi']
    list_editable = ['aktif', 'urutan']
    ordering = ['urutan']

@admin.register(Pengumuman)
class PengumumanAdmin(admin.ModelAdmin):
    list_display = ['judul', 'prioritas', 'aktif', 'tanggal_mulai', 'tanggal_berakhir']
    list_filter = ['prioritas', 'aktif', 'tanggal_mulai']
    search_fields = ['judul', 'isi']
    list_editable = ['aktif', 'prioritas']
    date_hierarchy = 'tanggal_mulai'
    
    fieldsets = (
        (None, {
            'fields': ('judul', 'isi', 'prioritas')
        }),
        ('Pengaturan Tampil', {
            'fields': ('aktif', 'tanggal_mulai', 'tanggal_berakhir')
        }),
    )

@admin.register(ProfilDesa)
class ProfilDesaAdmin(admin.ModelAdmin):
    list_display = ['nama_desa', 'kepala_desa', 'telepon', 'email']
    search_fields = ['nama_desa', 'kepala_desa']
    
    fieldsets = (
        ('Informasi Dasar', {
            'fields': ('nama_desa', 'kepala_desa', 'alamat', 'telepon', 'email', 'website')
        }),
        ('Deskripsi', {
            'fields': ('deskripsi_singkat', 'visi', 'misi')
        }),
        ('Media', {
            'fields': ('logo', 'foto_kantor')
        }),
    )

@admin.register(StatistikDesa)
class StatistikDesaAdmin(admin.ModelAdmin):
    list_display = ['tahun_data', 'jumlah_penduduk', 'jumlah_kk', 'luas_wilayah', 'diupdate']
    list_filter = ['tahun_data']
    ordering = ['-tahun_data']
