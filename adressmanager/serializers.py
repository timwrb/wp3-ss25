from rest_framework import serializers


class AdressSerializer(serializers.Serializer):
    anrede = serializers.CharField(max_length=5)
    firstname = serializers.CharField(max_length=15)
    lastname = serializers.CharField(max_length=15)
    street = serializers.CharField(max_length=30)
    house_number = serializers.CharField(max_length=5)
    postal_code = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def get_delivery_zone(self,address):
        if str(address.zip).startswith('7') or str(address.zip).startswith('8'):
            return 'SOUTH_GERMANY'
        elif str(address.zip).startswith('0') or str(address.zip).startswith('3') or str(address.zip).startswith('4') or str(address.zip).startswith('5') or str(address.zip).startswith('6') or str(address.zip).startswith('9'):
            return 'CENTRAL_GERMANY'
        elif str(address.zip).startswith('2') or str(address.zip).startswith('1'):
            return "NORTH_GERMANY"

    