from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.db.models import Sum
from productos.models import ProductoRandom
from productos.serializers import ProductoSerializer, ProductoRandomSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class ProdViewSet(viewsets.ModelViewSet):
    queryset = ProductoRandom.objects.all()
    serializer_class = ProductoRandomSerializer
    @action(
        methods=['GET'],
        detail=False,
        url_path='get-producto',
        url_name='get-producto'
    )
    def get_producto(self, request):
        queryset = ProductoRandom.objects.using('d1').all().values()

            

        serializer = ProductoRandomSerializer(queryset, many=True)
        return Response(serializer.data)
# Create your views here.
