from rest_framework import viewsets, permissions
from .models import Articulo, Proveedor
from .serializers import (
    ArticuloPublicSerializer,
    ArticuloSerializer,
    ProveedorPublicSerializer,
    ProveedorSerializer,
)
<<<<<<< HEAD

# GET all = list() 
# GET by id/pk = retrieve() -> RetrieveModelMixin
# POST = create()
# PUT = update() -> UpdateModelMixin
# DELETE = destroy() -> DestroyModelMixin

=======
# Vistas basadas en clases Concrete generic:
# List -> GET all
# Create -> POST
# Retrieve -> GET by id/pk
# Update -> PUT
# Destroy -> Delete

>>>>>>> 4258492eabc3b27888c830d3b57420bf9f0d97cf
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