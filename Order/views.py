from rest_framework import viewsets, permissions, generics

from django import views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Plate, Menu, DaySpecial, Order
from django.contrib.auth.models import User

from .serializers import PlateSerializer, MenuSerializer, DaySpecialSerializer, OrderSerializer, UserSerializer


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
