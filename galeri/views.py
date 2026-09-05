from django.shortcuts import render
from .models import Galeri

def galeri_list(request):
    galeri = Galeri.objects.filter(aktif=True)
    return render(request, 'galeri/list.html', {'galeri': galeri})
