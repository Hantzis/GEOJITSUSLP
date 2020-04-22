from django.contrib import admin
from .models import WMSServer, WMSLayer, WMSCRS, Project

# Register your models here.

admin.site.register(WMSServer)
admin.site.register(WMSLayer)
admin.site.register(WMSCRS)
admin.site.register(Project)