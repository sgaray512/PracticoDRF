<<<<<<< HEAD
from django.urls import path, include

from . import views
=======
from django.urls import path
from .views import (
    ProveedorListCreateAPIView, ProveedorDetailAPIView,
    ArticuloListCreateAPIView, ArticuloDetailAPIView
)
>>>>>>> 4258492eabc3b27888c830d3b57420bf9f0d97cf

urlpatterns = [
    path('proveedores/', ProveedorListCreateAPIView.as_view(), name='proveedor-list'),
    path('proveedores/<int:pk>/', ProveedorDetailAPIView.as_view(), name='proveedor-detail'),
    path('articulos/', ArticuloListCreateAPIView.as_view(), name='articulo-list'),
    path('articulos/<int:pk>/', ArticuloDetailAPIView.as_view(), name='articulo-detail'),
]