from django.shortcuts import render
from .models import Berita, KategoriBerita

def berita_list(request):
    berita = Berita.objects.filter(aktif=True)
    return render(request, 'berita/list.html', {'berita': berita})

def berita_detail(request, slug):
    berita = Berita.objects.get(slug=slug, aktif=True)
    return render(request, 'berita/detail.html', {'berita': berita})
