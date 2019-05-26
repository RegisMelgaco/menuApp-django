from rest_framework import serializers

from .models import Plate, Menu, DaySpecial, Order


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
