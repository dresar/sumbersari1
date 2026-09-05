from django.db import models
from django.urls import reverse

class KategoriBerita(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Kategori Berita'
        verbose_name_plural = 'Kategori Berita'
    
    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    konten = models.TextField()
    ringkasan = models.TextField(max_length=300)
    gambar = models.ImageField(upload_to='berita/')
    kategori = models.ForeignKey(KategoriBerita, on_delete=models.CASCADE)
    penulis = models.CharField(max_length=100)
    tanggal_publish = models.DateTimeField()
    aktif = models.BooleanField(default=True)
    dibuat = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-tanggal_publish']
        verbose_name = 'Berita'
        verbose_name_plural = 'Berita'
    
    def __str__(self):
        return self.judul
