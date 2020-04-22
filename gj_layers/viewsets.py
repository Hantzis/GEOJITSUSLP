from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from . models import WMSServer, WMSLayer, WMSCRS
from . serializers import WMSServerSerializer, WMSLayerSerializer, WMSCRSSerializer
from django_filters.rest_framework import DjangoFilterBackend

class WMSServerViewSet(ModelViewSet):
    queryset = WMSServer.objects.all()
    serializer_class = WMSServerSerializer

    def get_queryset(self):
        queryset = WMSServer.objects.all()
        project = self.request.query_params.get('project', None)
        if project:
            queryset = WMSServer.objects.filter(project=project)
        return queryset


class WMSLayerViewSet(ModelViewSet):
    queryset = WMSLayer.objects.all()
    serializer_class = WMSLayerSerializer
    # filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = WMSLayer.objects.all()
        project = self.request.query_params.get('project', None)
        if project:
            queryset = WMSLayer.objects.filter(server__project=project)
        return queryset


class WMSCRSViewSet(ReadOnlyModelViewSet):
    queryset = WMSCRS.objects.all()
    serializer_class = WMSCRSSerializer