from rest_framework_gis.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField, RelatedField
from . models import WMSServer, WMSLayer, WMSCRS


class WMSServerSerializer(ModelSerializer):
    class Meta:
        model = WMSServer
        fields = '__all__'


class WMSServerURL(RelatedField):
    def to_representation(self, value):
        return value.server_baseurl

class WMSLayerSerializer(ModelSerializer):
    server = WMSServerURL(many=False, read_only=True)

    class Meta:
        model = WMSLayer
        fields = '__all__'


class WMSCRSSerializer(ModelSerializer):
    class Meta:
        model = WMSCRS
        fields = '__all__'