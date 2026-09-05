from django.db import models
from django.urls import reverse

class Slider(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='slider/')
    link = models.URLField(blank=True, null=True)
    aktif = models.BooleanField(default=True)
    urutan = models.IntegerField(default=0)
    dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['urutan']
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.judul

class Pengumuman(models.Model):
    PRIORITY_CHOICES = [
        ('rendah', 'Rendah'),
        ('sedang', 'Sedang'),
        ('tinggi', 'Tinggi'),
        ('urgent', 'Urgent'),
    ]
    
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    prioritas = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='sedang')
    aktif = models.BooleanField(default=True)
    tanggal_mulai = models.DateTimeField()
    tanggal_berakhir = models.DateTimeField()
    dibuat = models.DateTimeField(auto_now_add=True)
    diupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tanggal_mulai']
        verbose_name = 'Pengumuman'
        verbose_name_plural = 'Pengumuman'

    def __str__(self):
        return self.judul

class ProfilDesa(models.Model):
    nama_desa = models.CharField(max_length=100)
    kepala_desa = models.CharField(max_length=100)
    alamat = models.TextField()
    telepon = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    deskripsi_singkat = models.TextField()
    visi = models.TextField()
    misi = models.TextField()
    logo = models.ImageField(upload_to='profil/', blank=True)
    foto_kantor = models.ImageField(upload_to='profil/', blank=True)
    
    class Meta:
        verbose_name = 'Profil Desa'
        verbose_name_plural = 'Profil Desa'

    def __str__(self):
        return self.nama_desa

class StatistikDesa(models.Model):
    jumlah_penduduk = models.IntegerField()
    jumlah_kk = models.IntegerField()
    luas_wilayah = models.DecimalField(max_digits=10, decimal_places=2)
    jumlah_rt = models.IntegerField()
    jumlah_rw = models.IntegerField()
    tahun_data = models.IntegerField()
    diupdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Statistik Desa'
        verbose_name_plural = 'Statistik Desa'

    def __str__(self):
        return f"Statistik {self.tahun_data}"
