from django.db import models

class KategoriLayanan(models.Model):
    nama = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome class")
    
    class Meta:
        verbose_name = 'Kategori Layanan'
        verbose_name_plural = 'Kategori Layanan'
    
    def __str__(self):
        return self.nama

class Layanan(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(KategoriLayanan, on_delete=models.CASCADE)
    persyaratan = models.TextField()
    prosedur = models.TextField()
    waktu_penyelesaian = models.CharField(max_length=100)
    biaya = models.CharField(max_length=100)
    aktif = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Layanan'
        verbose_name_plural = 'Layanan'
    
    def __str__(self):
        return self.nama
