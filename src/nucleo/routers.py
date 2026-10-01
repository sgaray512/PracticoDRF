from rest_framework.routers import DefaultRouter

from catalogo.views import ArticuloViewSet, ProveedorViewSet

router = DefaultRouter()

router.register("articulos", ArticuloViewSet, basename="articulos_vs")
router.register("proveedor", ProveedorViewSet, basename="proveedor_vs")