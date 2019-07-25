from django.db import models

# Create your models here.
<<<<<<< HEAD
class VocabsIndo(models.Model):
    indo = models.CharField(max_length=50)
    arti = models.TextField()
    related = models.TextField(null=True)
    sinonim = models.TextField(null=True)
=======

class Artikel(models.Model):
    foto = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)
    tanggal = models.DateField()
    isi = models.TextField()
    kategori = models.CharField(max_length=100, default='0000000')
>>>>>>> origin/dev
