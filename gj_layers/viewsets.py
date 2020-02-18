from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from . models import WMSServer, WMSLayer, WMSCRS
from . serializers import WMSServerSerializer, WMSLayerSerializer, WMSCRSSerializer


class WMSServerViewSet(ModelViewSet):
    queryset = WMSServer.objects.all()
    serializer_class = WMSServerSerializer


class WMSLayerViewSet(ModelViewSet):
    queryset = WMSLayer.objects.all()
    serializer_class = WMSLayerSerializer


class WMSCRSViewSet(ReadOnlyModelViewSet):
    queryset = WMSCRS.objects.all()
    serializer_class = WMSCRSSerializer