import json
import uuid

from django.http import JsonResponse
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
    #return Response()

@api_view(['POST'])
def add_product(request):
    try:
        data = json.loads(request.body.decode())
        product_id = uuid.uuid4()
        cb_models.Products.objects.create(
           id=product_id,
           title= data["title"],
           cost=data["cost"])

        return JsonResponse({
            'id': product_id
        })
    except :
        return JsonResponse({'error': 'Произошла ошибка'}, status=400)

def get_Product_by_id(request):
    Product_id = request.GET['id']

    Product = cb_models.Products.objects.get(id=Product_id)

    return JsonResponse({
        'title': Product.title
    },status=200)

@api_view(["POST"])
def update_Product_data(request):
    try:
        data = json.loads(request.body.decode())
        Product = cb_models.Products.objects.get(id=data["id"])
        Product.title = data["title"]
        Product.cost = data["cost"]
        #Product.group_id = data["group_id"]
        Product.save()

        return JsonResponse({
            'response': "Данные продукта успешно обновлены"
        })
    except :
        return JsonResponse({'error': 'Произошла ошибка'}, status=400)

@api_view(["POST"])
def calculate_material(request):
    try:
        data = json.loads(request.body.decode())
        rostovka = cb_models.Rostovka.objects.get(id_product=data["id"],size=data["size"])
        material_quantity=rostovka.expended_material*data["count"]
        product=cb_models.Products.objects.get(id=data["id"])
        material = cb_models.Material.objects.get(id=product.id_material)
        return JsonResponse({
            "material_name":material.title,
            "quantity":material_quantity
        })
    except:pass

# Create your views here.
