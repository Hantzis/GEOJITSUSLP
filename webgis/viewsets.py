from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Municipio, Ejido, Parcela
from .serializers import MunicipioSerializer, EjidoSerializer, ParcelaSerializer, ParcelaNombreSerializer


class MunicipioViewSet(ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class EjidoViewSet(ModelViewSet):
    queryset = Ejido.objects.all()
    serializer_class = EjidoSerializer


class ParcelaViewSet(ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer

class ParcelaNombreViewSet(ReadOnlyModelViewSet):
    queryset = Parcela.objects.all().order_by('nombre_parcela')
    serializer_class = ParcelaNombreSerializer