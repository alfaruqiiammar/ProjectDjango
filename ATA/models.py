from django.db import models

# Create your models here.

class Artikel(models.Model):
    foto = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)
    tanggal = models.DateField()
    isi = models.TextField()
    kategori = models.CharField(max_length=100, default='0000000')
