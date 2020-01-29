from django.contrib.gis.db import models

# Create your models here.


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=255, unique=True)
    geom = models.MultiPolygonField(srid=3857)


class Ejido(models.Model):
    clave_unica = models.PositiveIntegerField()
    nombre_ejido = models.CharField(max_length=255, unique=True)
    geom = models.MultiPolygonField(srid=3857)


class Parcela(models.Model):
    nombre_parcela = models.CharField(max_length=255, unique=True)
    nombre_propietario = models.CharField(max_length=255, unique=True)
    programa = models.CharField(max_length=255, unique=True)
    geom = models.MultiPolygonField(srid=3857)

