from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view()
def get_product_by_id(request, id):
    product = products.objects.get(id=id)
    return Response(f"Nummer: {product.id}, Name: {product.product_name}, Brutto Preis: {product.priceB}€, Netto Preis: {product.priceN}€<br>")



def get_all_products(request):
    Products = get_list_or_404(products)

    response = ""
    for product in Products:
        response += f"Nummer: {product.id}, Name: {product.product_name}, Brutto Preis: {product.priceB}€, Netto Preis: {product.priceN}€<br>"

    return HttpResponse(response)
        
