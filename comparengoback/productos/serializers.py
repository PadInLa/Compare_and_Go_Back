from django.contrib.auth.models import User, Group
from rest_framework import serializers
from productos.models import ProductoRandom

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoRandom
        fields = ['indice', 'nombre', 'precio', 'tienda']

class ProductoRandomSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    precio = serializers.CharField()
    tienda = serializers.CharField()

