from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

@api_view(['GET'])
def get_stock(request):
    try:
        # Product ID aus dem Request Body holen
        product_id = request.data.get('product_id')

        if not product_id:
            return Response(
                {'error': 'product_id is required in request body'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Stock für das Produkt suchen
        stock = Stock.objects.get(product_id=product_id)

        # Serializer verwenden um nur die gewünschten Felder zurückzugeben
        serializer = StockSerializer(stock)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Stock.DoesNotExist:
        return Response(
            {'error': 'Stock not found for this product'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )