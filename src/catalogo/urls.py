from django.urls import path
from .views import (
    ProveedorListCreateAPIView, ProveedorDetailAPIView,
    ArticuloListCreateAPIView, ArticuloDetailAPIView
)

urlpatterns = [
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list'),
    path('proveedores/<int:pk>/', ProveedorDetailAPIView.as_view(), name='proveedor-detail'),
    path('articulos/', ArticuloListCreateAPIView.as_view(), name='articulo-list'),
    path('articulos/<int:pk>/', ArticuloDetailAPIView.as_view(), name='articulo-detail'),
]