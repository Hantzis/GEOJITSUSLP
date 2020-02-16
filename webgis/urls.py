from rest_framework import routers

from .viewsets import MunicipioViewSet, EjidoViewSet, ParcelaViewSet, ParcelaNombreViewSet

router = routers.SimpleRouter()

router.register('municipios', MunicipioViewSet)
router.register('ejidos', EjidoViewSet)
router.register('parcelas', ParcelaViewSet)
router.register('parcelas_nombre', ParcelaNombreViewSet)

urlpatterns = router.urls


