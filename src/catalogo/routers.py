from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, ProveedorViewSet  # <--- Importa tus clases reales

router = DefaultRouter()

# Registra los ViewSets con sus nombres de endpoint correspondientes
router.register(r'articulos', ArticuloViewSet, basename='articulo')
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')

urlpatterns = router.urls