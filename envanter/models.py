from django.db import models
from django.contrib.auth.models import User # User modelini import ediyoruz

class Firma(models.Model):
    ad = models.CharField(max_length=200)

    def __str__(self):
        return self.ad

class Parca(models.Model):
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, related_name='parcalar')
    ad = models.CharField(max_length=200, blank=True, null=True)
    adet = models.IntegerField()
    renk = models.CharField(max_length=100)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    ekleyen_kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # Yeni alan

    def __str__(self):
        return self.ad

class Fotograf(models.Model):
    parca = models.ForeignKey(Parca, on_delete=models.CASCADE, related_name='fotograflar')
    resim = models.ImageField(upload_to='parca_fotograflari/')

    def __str__(self):
        return f"{self.parca.ad} - Fotoğraf"