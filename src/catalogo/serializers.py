from rest_framework import serializers
from .models import Articulo, Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
        read_only_fields = ["id"]

class ProveedorPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["nombre", "telefono"]
        read_only_fields = ["id"]

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [
            "id",
            "marca",
            "modelo",
            "nombre",
            "precio",
            "stock",
            "timestamp",
            "proveedor",
        ]
        read_only_fields = ["id", "timestamp"]

class ArticuloPublicSerializer(serializers.ModelSerializer):
    proveedor = ProveedorPublicSerializer(read_only=True)
    
    class Meta:
        model = Articulo
        fields = [
            "id",
            "modelo",
            "nombre",
            "precio",
            "proveedor",
        ]
        read_only_fields = ["id"]