from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("id","nombre","descripcion","precio_compra","precio_venta","existencias","fecha_reg")
        read_only_fields = ("fecha_reg",)