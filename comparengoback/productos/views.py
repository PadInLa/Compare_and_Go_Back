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
from productos.utils import flatten_list

class ProdViewSet(viewsets.ModelViewSet): 
    queryset = ProductoRandom.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        results = []
        queryset = ProductoRandom.objects.all().annotate(
            float_price=Coalesce(Cast(F('precio'), FloatField()), 0.0)
        ).order_by('float_price')
        product_name = request.GET.get('productName', None)

        if product_name:
            queryset = queryset.filter(nombre__icontains=product_name)

        tienda_name = set(queryset.values_list('tienda', flat=True))
        for tienda in tienda_name:
            results.append(list(queryset.filter(tienda=tienda).values_list('id', flat=True))[:5])
        
        results = flatten_list(results)

        queryset = queryset.filter(id__in=results)  
        
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
