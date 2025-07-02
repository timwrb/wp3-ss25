from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from productmanager.models import Product
from productmanager.serializers import ProductSerializer

# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def show_all_products(request):
    if request.method == "GET":
        searchterm = request.query_params.get("searchterm")
        maxprice = request.query_params.get("maxprice")

        if searchterm is not None and maxprice is not None:
            products = get_list_or_404(Product, name__icontains=searchterm, price_brutto__lte=maxprice)
        elif maxprice is not None:
            products = get_list_or_404(Product, price_brutto__lte=maxprice)
        elif searchterm is not None:
            products = get_list_or_404(Product, name__icontains=searchterm)
        else:
            products = get_list_or_404(Product)

        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)
    elif request.method == "POST":
        if request.user.is_staff:
            product_serializer = ProductSerializer(data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def show_product_by_id(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "GET":
        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data)
    elif request.method == "DELETE":
        if request.user.is_staff:
            product.delete()
            return Response(data={"msg": "The resource has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied
    elif request.method == "PUT":
        if request.user.is_staff:
            product_serializer = ProductSerializer(instance=product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data)
            return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied

