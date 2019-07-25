from django.contrib import admin
from .models import VocabsIndo

# Register your models here.
<<<<<<< HEAD
admin.site.register(VocabsIndo)
=======

from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'tanggal']  
    list_display_links = ['judul']


admin.site.register(Artikel, ArtikelAdmin)
>>>>>>> origin/dev
