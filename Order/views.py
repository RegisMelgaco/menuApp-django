from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Plate, Menu
from .serializers import PlateSerializer, MenuSerializer


class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAuthenticated, )
