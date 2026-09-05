from django.db import models

class Galeri(models.Model):
    TIPE_CHOICES = [
        ('foto', 'Foto'),
        ('video', 'Video'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    tipe = models.CharField(max_length=10, choices=TIPE_CHOICES)
    file = models.ImageField(upload_to='galeri/', blank=True)
    video_url = models.URLField(blank=True)
    tanggal = models.DateField()
    aktif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-tanggal']
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'
    
    def __str__(self):
        return self.judul
