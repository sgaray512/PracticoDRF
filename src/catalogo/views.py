from rest_framework import viewsets, permissions
from .models import Articulo, Proveedor
from .serializers import (
    ArticuloPublicSerializer,
    ArticuloSerializer,
    ProveedorPublicSerializer,
    ProveedorSerializer,
)
# Vistas basadas en clases Concrete generic:
# List -> GET all
# Create -> POST
# Retrieve -> GET by id/pk
# Update -> PUT
# Destroy -> Delete

# VISTAS PROVEEDOR
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.IsAuthenticated] # Protege todas las acciones con JWT

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProveedorPublicSerializer
        return ProveedorSerializer


# VISTAS ARTÍCULO
class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    # Permite lectura pública pero requiere autenticación (Token) para crear/editar/eliminar
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ArticuloPublicSerializer
        return ArticuloSerializer