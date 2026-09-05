from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Slider, Pengumuman, ProfilDesa, StatistikDesa

def index(request):
    """Halaman utama website desa"""
    # Ambil slider aktif
    sliders = Slider.objects.filter(aktif=True)[:5]
    
    # Ambil pengumuman aktif
    pengumuman_list = Pengumuman.objects.filter(
        aktif=True,
        tanggal_mulai__lte=timezone.now(),
        tanggal_berakhir__gte=timezone.now()
    )[:3]
    
    # Ambil profil desa
    try:
        profil = ProfilDesa.objects.first()
    except ProfilDesa.DoesNotExist:
        profil = None
    
    # Ambil statistik terbaru
    try:
        statistik = StatistikDesa.objects.latest('tahun_data')
    except StatistikDesa.DoesNotExist:
        statistik = None

    context = {
        'sliders': sliders,
        'pengumuman_list': pengumuman_list,
        'profil': profil,
        'statistik': statistik,
    }
    return render(request, 'home/index.html', context)

def tentang(request):
    """Halaman tentang desa"""
    try:
        profil = ProfilDesa.objects.first()
    except ProfilDesa.DoesNotExist:
        profil = None
    
    try:
        statistik = StatistikDesa.objects.latest('tahun_data')
    except StatistikDesa.DoesNotExist:
        statistik = None

    context = {
        'profil': profil,
        'statistik': statistik,
    }
    return render(request, 'home/tentang.html', context)

def pengumuman_list(request):
    """Daftar semua pengumuman"""
    pengumuman_list = Pengumuman.objects.filter(aktif=True)
    
    # Pagination
    paginator = Paginator(pengumuman_list, 10)
    page_number = request.GET.get('page')
    pengumuman = paginator.get_page(page_number)
    
    context = {
        'pengumuman': pengumuman,
    }
    return render(request, 'home/pengumuman.html', context)

def pengumuman_detail(request, id):
    """Detail pengumuman"""
    pengumuman = get_object_or_404(Pengumuman, id=id, aktif=True)
    
    context = {
        'pengumuman': pengumuman,
    }
    return render(request, 'home/pengumuman_detail.html', context)

def kontak(request):
    """Halaman kontak"""
    try:
        profil = ProfilDesa.objects.first()
    except ProfilDesa.DoesNotExist:
        profil = None

    context = {
        'profil': profil,
    }
    return render(request, 'home/kontak.html', context)
