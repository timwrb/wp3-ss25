from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from shoppingcart.models import Customer
from shoppingcart.serializers import CustomerSerializers


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_all_customers(request):

    if request.method == "GET":
        if request.user.is_staff:
            firstname = request.query_params.get("firstname")
            lastname = request.query_params.get("lastname")

            if firstname is not None and lastname is not None:
                customers = get_list_or_404(Customer, firstname__contains=firstname, lastname__contains=lastname)
            elif firstname is not None:
                customers = get_list_or_404(Customer, firstname__contains=firstname)
            elif lastname is not None:
                customers = get_list_or_404(Customer, lastname__contains=lastname)
            else:
                customers = get_list_or_404(Customer)

            serialized_customers = CustomerSerializers(customers, many=True)
            return Response(serialized_customers.data)
        else:
            raise PermissionDenied
    elif request.method == "POST":
        customer_serializer = CustomerSerializers(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save(user_id = request.data["user"], id = request.data["user"])
            return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def get_customer_details(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.user == customer.user or request.user.is_staff:
        if request.method == "GET":
            serialized_customer = CustomerSerializers(customer)
            return Response(serialized_customer.data)
        elif request.method == "PUT":
            serializer = CustomerSerializers(instance=customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            customer.delete()
            return Response(data={"success": "Resource deleted"}, status=status.HTTP_204_NO_CONTENT)
    else:
        raise PermissionDenied
