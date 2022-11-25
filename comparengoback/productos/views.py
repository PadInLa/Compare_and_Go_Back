from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.db.models import Sum
from productos.models import ProductoRandom
from productos.serializers import ProductoSerializer
from django.contrib.postgres.search import SearchVector
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import Coalesce, Cast
from django.db.models import F, FloatField

class ProdViewSet(viewsets.ModelViewSet): 
    queryset = ProductoRandom.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        queryset = ProductoRandom.objects.all().annotate(
            float_price=Coalesce(Cast(F('precio'), FloatField()), 0.0)
        ).order_by('float_price')
        product_name = request.GET.get('productName', None)
        if product_name:
            queryset = queryset.filter(nombre__icontains=product_name)
        
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
