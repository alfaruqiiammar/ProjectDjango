from django.db import models

# Create your models here.
class VocabsIndo(models.Model):
    indo = models.CharField(max_length=50)
    arti = models.TextField()
    related = models.TextField(null=True)
    sinonim = models.TextField(null=True)
