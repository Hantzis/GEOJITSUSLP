from django.contrib import admin
from .models import WMSServer, WMSLayer

# Register your models here.

admin.site.register(WMSServer)
admin.site.register(WMSLayer)