from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import cbApp.models as cb_models
import cbApp.serializer as serializer


@api_view(['GET'])
def getALLProducts(request):
    products = cb_models.Products.objects.all()
    srlz = serializer.ProductSerializer(products, many=True)
    return Response(srlz.data)

# Create your views here.
