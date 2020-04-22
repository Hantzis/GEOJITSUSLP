from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from . models import WMSServer, WMSLayer, WMSCRS
from . serializers import WMSServerSerializer, WMSLayerSerializer, WMSCRSSerializer
from django_filters.rest_framework import DjangoFilterBackend

class WMSServerViewSet(ModelViewSet):
    queryset = WMSServer.objects.all()
    serializer_class = WMSServerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['project', 'id']


class WMSLayerViewSet(ModelViewSet):
    queryset = WMSLayer.objects.all()
    serializer_class = WMSLayerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['server__project', 'id']


class WMSCRSViewSet(ReadOnlyModelViewSet):
    queryset = WMSCRS.objects.all()
    serializer_class = WMSCRSSerializer