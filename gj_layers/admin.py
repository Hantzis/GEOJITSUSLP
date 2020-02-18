from django.contrib import admin
from .models import WMSServer, WMSLayer, WMSCRS

# Register your models here.

admin.site.register(WMSServer)
admin.site.register(WMSLayer)
admin.site.register(WMSCRS)