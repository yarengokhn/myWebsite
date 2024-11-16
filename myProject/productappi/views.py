from django.http import JsonResponse
from django.shortcuts import render
from product.models import Product
from productappi.serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    #adim1
    # products =Product.objects.all()
    # products_list = list(products.values())
    # return JsonResponse({'products':products_list})
    #adim2 
    # products =Product.objects.all()
    # serializer=ProductSerializer(products,many=True)
    # return JsonResponse(serializer.data,safe=False)

    # adim3
    products =Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_product(request,id):
    try:
        product =Product.objects.get(pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist as e:
        return Response({'error':f'Product bulunamadi {e}'},status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','DELETE']) #ilk ürünü alsin sonra silsin
def delete_product(request,id):
    try:
        product =Product.objects.get(pk=id)
        product.delete()
        return Response({'message':'Product silindi.'},status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist as e :
        return Response({'error':f'Product silindi.{e}'},status=status.HTTP_204_NO_CONTENT)
    



@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

