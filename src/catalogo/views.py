from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
class ProveedorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProveedorPublicSerializer
        return ProveedorSerializer

class ProveedorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# VISTAS ARTÍCULO
class ArticuloListCreateAPIView(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticuloPublicSerializer
        return ArticuloSerializer

class ArticuloDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer