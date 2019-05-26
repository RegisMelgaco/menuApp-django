from rest_framework import viewsets, permissions

from .models import Plate, Menu, DaySpecial
from .serializers import PlateSerializer, MenuSerializer, DaySpecialSerializer


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
