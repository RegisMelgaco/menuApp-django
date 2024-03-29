from rest_framework import serializers

from .models import Plate, Menu, DaySpecial, Order, OrderHasPlate
from django.contrib.auth.models import User


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class DaySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySpecial
        fields = '__all__'


class OrderHasPlateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderHasPlate
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    itens = OrderHasPlateSerializer(source='orderhasplate_set', many=True)

    class Meta:
        model = Order
        exclude = ('plates',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
