from django.db import models
from PIL import Image


# Create your models here.
class Hospital(models.Model):
    nome_hospital = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_hospital = models.TextField(max_length=200)
    tipo_hospital = models.CharField(max_length=200)
    conceito_hospital = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        im = Image.open(self.foto.path)
        # novo_tamanho =
        im.thumbnail((300, 380))
        im.save(self.foto.path)

    def foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return "img/placeholder.png"

    def __str__(self):
        return self.nome_hospital
