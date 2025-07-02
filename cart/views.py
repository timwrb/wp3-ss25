from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from cart.models import Cart, Entry
from cart.serializers import CartSerializer, AddToCartSerializer
from productmanager.models import Product
from shoppingcart.models import Customer


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def show_cart(request):
    if request.method == "GET":
        cart = get_list_or_404(Cart)
        serialized_cart = CartSerializer(cart)
        return Response(serialized_cart.data)
    elif request.method == "POST":
        cart_serializer = CartSerializer(data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def show_cart_detail(request, id):
    cart = get_object_or_404(Cart, pk=id)
    if request.method == "GET":
        serialized_cart = CartSerializer(cart)
        return Response(serialized_cart.data)
    elif request.method == "DELETE":
        cart.delete()
        return Response(data="Cart deleted")
    elif request.method == "PUT":
        cart_serializer = CartSerializer(instance=cart, data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data)
        return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@permission_classes([AllowAny])
def add_to_cart(request):
    global cart
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.data.get('product_id')
        quantity = serializer.data.get('quantity')
        cart_id = serializer.data.get('cart_id')

        if cart_id is not None:
            cart = get_object_or_404(Cart, id=cart_id)
        else:
            if isinstance(request.user, AnonymousUser):
                print("Gast User")
                cart = Cart()
                cart.save()
            else:
                print("Registriert")

                customer = get_object_or_404(Customer, user_id=request.user_id)
                # check if logged in customer has a cart
                cart = Cart.objects.all().filter(customer_id=customer.id)[0]

                if not cart:
                    cart = Cart(customer_id=customer.id)
                    cart.save()
                else:
                    cart = cart[0]

        product = get_object_or_404(Product, id=product_id)
        cart_entry = Entry(
                            cart_id=cart.id,
                            product_id=product.id,
                            product_name=product.product_name,
                            net=product.price_net,
                            gross=product.price_gross,
                            quantity=quantity,
                            total_net=product.price_net * quantity,
                            total_gross=product.price_gross * quantity)
        cart_entry.save()

        cart.net += cart_entry.total_net
        cart.gross += cart_entry.total_gross
        cart.tax_value = cart.gross - cart.net

        cart.save()
        print(cart.gross)

        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors)

@api_view(['PUT'])
def convert_cart(request):
    cart_id = request.data.get('cart_id')
    user = request.user
    customer = get_object_or_404(Customer,user_id=user.id)
    cart = get_object_or_404(Cart, id=cart_id)
    cart.customer = customer
    cart.save()
    return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)
