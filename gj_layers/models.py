from django.db import models

# Create your models here.


class WMSServer(models.Model):
    server_name = models.CharField(max_length=255, unique=True)
    server_baseurl = models.URLField()

    # TODO: validar que la base url es un servidor WMS válido
     def __str__(self):
         return self.server_name


class WMSLayer(models.Model):
    layer_name = models.CharField(max_length=255, unique=True);
    server = models.ForeignKey(WMSServer, on_delete=models.PROTECT)

    def __str__(self):
        return self.layer_name