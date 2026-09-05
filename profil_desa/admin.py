from django.contrib import admin
from .models import SejarahDesa, StrukturOrganisasi

@admin.register(SejarahDesa)
class SejarahDesaAdmin(admin.ModelAdmin):
    list_display = ['judul', 'tahun']
    ordering = ['tahun']

@admin.register(StrukturOrganisasi)
class StrukturOrganisasiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'jabatan', 'urutan']
    list_editable = ['urutan']
