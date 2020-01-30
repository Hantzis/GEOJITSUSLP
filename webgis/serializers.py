from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoFeatureModelListSerializer
from . models import Municipio, Ejido, Parcela


class MunicipioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        geo_field = 'geom'
        id_field = 'id'


class EjidoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ejido
        fields = '__all__'
        geo_field = 'geom'


class ParcelaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'
        geo_field = 'geom'

