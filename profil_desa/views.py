from django.shortcuts import render
from .models import SejarahDesa, StrukturOrganisasi

def profil_desa(request):
    sejarah = SejarahDesa.objects.all()
    struktur = StrukturOrganisasi.objects.all()
    return render(request, 'profil_desa/profil.html', {
        'sejarah': sejarah,
        'struktur': struktur
    })
