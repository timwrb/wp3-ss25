from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from adressmanager.models import adresses
from adressmanager.serializers import AdressSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def show_all_addresses(request):
    if request.method == "GET":
        if request.user.is_staff:
            addresses = get_list_or_404(adresses)
            serialized_addresses = AdressSerializer(addresses, many=True)
            return Response(serialized_addresses.data)
        else:
            raise PermissionDenied
    elif request.method == "POST":
        address_serializer = AdressSerializer(data=request.data)
        if address_serializer.is_valid():
            address_serializer.save()
            return Response(address_serializer.data, status=status.HTTP_201_CREATED)
        return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def show_address_by_id(request, id):
    address = get_object_or_404(adresses, id=id)
    if request.user == address.user or request.user.is_staff:
        if request.method == "GET":
            serialized_address = AdressSerializer(address)
            return Response(serialized_address.data)
        elif request.method == "PUT":
            address_serializer = AdressSerializer(instance=address, data=request.data)
            if address_serializer.is_valid():
                address_serializer.save()
                return Response(address_serializer.data)
            return Response(address_serializer.errors, status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            address.delete()
            return Response(data={"msg": "The resource has been deleted"}, status=status.HTTP_204_NO_CONTENT)
    else:
        raise PermissionDenied
