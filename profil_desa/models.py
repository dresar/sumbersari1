from django.db import models

class SejarahDesa(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    tahun = models.IntegerField()
    
    class Meta:
        ordering = ['tahun']
        verbose_name = 'Sejarah Desa'
        verbose_name_plural = 'Sejarah Desa'
    
    def __str__(self):
        return f"{self.tahun} - {self.judul}"

class StrukturOrganisasi(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='struktur/', blank=True)
    urutan = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['urutan']
        verbose_name = 'Struktur Organisasi'
        verbose_name_plural = 'Struktur Organisasi'
    
    def __str__(self):
        return f"{self.nama} - {self.jabatan}"
