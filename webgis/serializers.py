from rest_framework import serializers
from . models import Municipio, Ejido, Parcela


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class EjidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejido
        fields = '__all__'


class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'

