from django.contrib.auth.models import User, Group
from rest_framework import serializers
from productos.models import ProductoRandom

class ProductoSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['precio'] = f"$ {float(data['precio']):,}" if data['precio'] else None
        return data
    class Meta:
        model = ProductoRandom
        fields = ['indice', 'nombre', 'precio', 'tienda']

        

