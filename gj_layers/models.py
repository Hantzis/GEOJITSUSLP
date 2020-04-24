from django.db import models
from owslib.wms import WebMapService
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class XYZLayer(models.Model):
    layer_name = models.CharField(max_length=255, unique=True)
    server = models.URLField()

    def __str__(self):
        return self.layer_name

    class Meta:
        ordering = ['id']


class WMSServer(models.Model):
    # el server_name debe ser unique con el usuario propietario (despues)
    server_name = models.CharField(max_length=255, unique=True)
    server_baseurl = models.URLField()
    server_version = models.CharField(max_length=5,
                                      choices=(('', 'WMS Version'), ('1.1.1', '1.1.1'), ('1.3.0', '1.3.0')))
    server_title = models.CharField(max_length=255)
    server_abstract = models.CharField(max_length=255, blank=True, null=True)
    server_enabled = models.BooleanField(default=True)
    server_permanent = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.server_name

    def save(self, *args, **kwargs):
        if self.server_baseurl[-1] != '?':  # Revisar si la url termina con un signo '?'
            self.server_baseurl += '?'  # Si no, ponerselo, es necesario para concatenar los demas parametros
        try:
            wms = WebMapService(self.server_baseurl, self.server_version)
            if not self.server_title:
                self.server_title = wms.identification.title
            if not self.server_abstract:
                self.server_abstract = wms.identification.title

            super(WMSServer, self).save(*args, **kwargs)
        except Exception as error:
            raise ValidationError(error)


class WMSCRS(models.Model):
    crs = models.CharField(max_length=20, unique=True, primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    # poner descripción

    def __str__(self):
        return "{} - {}".format(self.crs, self.description)

    class Meta:
        ordering = ['crs']


class WMSLayer(models.Model):
    # el layer_name debe ser unique con el usuario propietario (despues)
    layer_name = models.CharField(max_length=255, unique=True)
    layer_description = models.CharField(max_length=255, blank=True, null=True)
    layer_enabled = models.BooleanField(default=False)
    layer_permanent = models.BooleanField(default=False)
    # layer_visible = models.BooleanField(default=False)
    layer_opacity = models.PositiveSmallIntegerField(default=100)
    layer_order = models.PositiveSmallIntegerField(default=0)
    server = models.ForeignKey(WMSServer, on_delete=models.PROTECT)
    version = models.CharField(max_length=5, choices=(('', 'WMS Version'), ('1.1.1', '1.1.1'), ('1.3.0', '1.3.0')))
    layers = models.CharField(max_length=255)
    styles = models.CharField(max_length=255, blank=True, null=True)
    crs = models.ForeignKey(WMSCRS, on_delete=models.PROTECT, default='EPSG:4326')
    format = models.CharField(max_length=50, choices=(('', 'Image Format'), ('image/gif', 'image/gif'),
                                                      ('image/jpeg', 'image/jpeg'), ('image/png', 'image/png'),
                                                      ('image/png8', 'image/png8 (Recommended)'),
                                                      ('image/vnd.jpeg-png', 'image/vnd.jpeg-png'),
                                                      ('image/vnd.jpeg-png8', 'image/vnd.jpeg-png8')))
    transparent = models.BooleanField(default=True)
    sld = models.CharField(max_length=255, blank=True, null=True,
                           verbose_name='sld')  # tal vez haya que cambiar a texto
    time = models.DateTimeField(null=True, blank=True)
    cql_filter = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['layer_order', 'id']

    def save(self, *args, **kwargs):
        try:
            wms = WebMapService(self.server.server_baseurl, self.server.server_version)
            self.version = self.server.server_version
            if self.layers not in list(wms.contents):
                raise ValidationError("Layer don't exists")
            super(WMSLayer, self).save(*args, **kwargs)
        except Exception as error:
            raise ValidationError(error)

    def __str__(self):
        return self.layer_name
