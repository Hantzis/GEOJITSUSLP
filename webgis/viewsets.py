from rest_framework.viewsets import ModelViewSet

from .models import Municipio, Ejido, Parcela
from .serializers import MunicipioSerializer, EjidoSerializer, ParcelaSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie


class CacheMixin:
    @method_decorator(cache_page(360 * 360 * 2))
    def get(self, request, *args, **kwargs):
        return super(CacheMixin).get(self, request, *args, **kwargs)

    @method_decorator(cache_page(360 * 360 * 2))
    def list(self, request, *args, **kwargs):
        return list(CacheMixin).get(self, request, *args, **kwargs)

class MunicipioViewSet(CacheMixin, ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class EjidoViewSet(CacheMixin, ModelViewSet):
    queryset = Ejido.objects.all()
    serializer_class = EjidoSerializer


class ParcelaViewSet(CacheMixin, ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer
