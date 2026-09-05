from django.shortcuts import render
from .models import Layanan, KategoriLayanan

def layanan_list(request):
    layanan = Layanan.objects.filter(aktif=True)
    kategori = KategoriLayanan.objects.all()
    return render(request, 'layanan/list.html', {
        'layanan': layanan,
        'kategori': kategori
    })

def layanan_detail(request, id):
    layanan = Layanan.objects.get(id=id, aktif=True)
    return render(request, 'layanan/detail.html', {'layanan': layanan})
