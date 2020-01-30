from django.contrib import admin
from . models import Municipio, Ejido, Parcela
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

admin.site.register(Municipio, OSMGeoAdmin)
admin.site.register(Ejido, OSMGeoAdmin)
admin.site.register(Parcela, OSMGeoAdmin)