from rest_framework import routers

from . viewsets import WMSServerViewSet, WMSLayerViewSet, WMSCRSViewSet

router = routers.SimpleRouter()

router.register('wms-servers', WMSServerViewSet)
router.register('wms-layers', WMSLayerViewSet)
router.register('wms-crs', WMSCRSViewSet)

urlpatterns = router.urls


