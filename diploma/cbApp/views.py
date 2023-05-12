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
        Product.id_material = data["material_id"]
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

        is_enougth = material.stock_balance > material_quantity

        if not is_enougth:
            required = material_quantity - material.stock_balance
            required_cost = required * material.cost_per_square_meter

            return JsonResponse({
                "material_name": material.title,
                "quantity": material_quantity,
                "is_enougth": is_enougth,
                "diff": required,
                "diff_cost": required_cost
            })

        return JsonResponse({
            "material_name":material.title,
            "quantity":material_quantity,
            "is_enougth": is_enougth
        })
    except:pass

@api_view(['POST'])
def add_rostovka(request):
    try:
        data = json.loads(request.body.decode())
        rostovka_id = uuid.uuid4()
        cb_models.Rostovka.objects.create(
            id=rostovka_id,
            size=data["size"],
            expended_material=data["expended_material"],
            id_product= data["product_id"])

        return JsonResponse({
            'id': rostovka_id
            })
    except:
        return JsonResponse({'error': 'Произошла ошибка'}, status=400)

@api_view(['POST'])
def add_material(request):
    try:
        data = json.loads(request.body.decode())
        material_id = uuid.uuid4()
        cb_models.Material.objects.create(
           id=material_id,
           title= data["title"],
           stock_balance=data["stock_balance"],
           cost_per_square_meter=data["cost_per_square_meter"])

        return JsonResponse({
            'id': material_id
        })
    except :
        return JsonResponse({'error': 'Произошла ошибка'}, status=400)

# Create your views here.
