from rest_framework.viewsets import ModelViewSet
from .models import Municipio, Ejido, Parcela
from .serializers import MunicipioSerializer, EjidoSerializer, ParcelaSerializer


class MunicipioViewSet(ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class EjidoViewSet(ModelViewSet):
    queryset = Ejido.objects.all()
    serializer_class = EjidoSerializer


class ParcelaViewSet(ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer
