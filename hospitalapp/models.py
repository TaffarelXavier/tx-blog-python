from django.db import models
from PIL import Image


# Create your models here.
class Hospital(models.Model):
    nome_hospital = models.TextField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_hospital = models.TextField(max_length=200)
    tipo_hospital = models.TextField(max_length=200)
    conceito_hospital = models.TextField(max_length=500)

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

# Posts models


class Post(models.Model):
    titulo = models.TextField(max_length=200)
    descricao = models.TextField(max_length=200)
    foto = models.ImageField(null=True, blank=True)

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
        return self.titulo


# Posts models
class TelaInicial(models.Model):
    titulo_cabebalho = models.TextField(max_length=200)
    titulo = models.TextField(max_length=200)
    descricao = models.TextField(max_length=200)
    
    box_1_titulo = models.TextField(null=True, blank=True)
    box_1_descricao = models.TextField(null=True, blank=True)
    box_1_foto = models.ImageField(null=True, blank=True)
    
    box_2_titulo = models.TextField(null=True, blank=True)
    box_2_descricao = models.TextField(null=True, blank=True)
    box_2_foto = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        im = Image.open(self.box_1_foto.path)
        im.thumbnail((300, 380))
        im.save(self.box_1_foto.path)

    def foto_url(self):
        if self.box_1_foto and hasattr(self.box_1_foto, 'url'):
            return self.box_1_foto.url
        else:
            return "img/placeholder.png"

    def __str__(self):
        return self.titulo
