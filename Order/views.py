from rest_framework import viewsets, permissions

from .models import Plate, Menu, DaySpecial, Order
from .serializers import PlateSerializer, MenuSerializer, DaySpecialSerializer, OrderSerializer


class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DaySpecialViewSet(viewsets.ModelViewSet):
    queryset = DaySpecial.objects.all()
    serializer_class = DaySpecialSerializer
    permission_classes = (permissions.IsAuthenticated, )


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, )
