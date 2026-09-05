from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('berita/', include('berita.urls')),
    path('profil/', include('profil_desa.urls')),
    path('layanan/', include('layanan.urls')),
    path('galeri/', include('galeri.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom admin titles
admin.site.site_header = "Admin Website Desa"
admin.site.site_title = "Portal Desa"
admin.site.index_title = "Selamat Datang di Admin Portal Desa"
