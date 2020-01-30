from django.contrib.gis.db import models

# Create your models here.


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=255, unique=True)
    geom = models.MultiPolygonField(srid=3857)

    def __str__(self):
        return self.nombre_municipio


class Ejido(models.Model):
    clave_unica = models.CharField(max_length=30)
    nombre_ejido = models.CharField(max_length=255)
    geom = models.MultiPolygonField(srid=3857)

    def __str__(self):
        return self.nombre_ejido

class Parcela(models.Model):
    nombre_parcela = models.CharField(max_length=255)
    nombre_propietario = models.CharField(max_length=255)
    programa = models.CharField(max_length=255)
    geom = models.MultiPolygonField(srid=3857)

    def __str__(self):
        return "{} - {}".format(self.nombre_parcela, self.nombre_propietario)
