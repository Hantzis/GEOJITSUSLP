from rest_framework_gis.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField
from . models import WMSServer, WMSLayer, WMSCRS


class WMSServerSerializer(ModelSerializer):
    class Meta:
        model = WMSServer
        fields = '__all__'


class WMSLayerSerializer(ModelSerializer):
    server = StringRelatedField(many=True)

    class Meta:
        model = WMSLayer
        fields = '__all__'


class WMSCRSSerializer(ModelSerializer):
    class Meta:
        model = WMSCRS
        fields = '__all__'