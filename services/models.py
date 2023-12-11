from django.db import models


class WhatsAppSettings(models.Model):
    id_instance = models.CharField(max_length=255)
    api_token_instance = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="Default Name")
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)


class Path(models.Model):
    path = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.path


class Proveedor(models.Model):
    token = models.TextField()
    nombre = models.CharField(max_length=255, unique=True)
    domain = models.TextField()
    descripcion = models.TextField()
    paths = models.ManyToManyField(Path)

    def __str__(self):
        return self.nombre