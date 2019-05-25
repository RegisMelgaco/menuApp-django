from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Plate
from .serializers import PlateSerializer


class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    permission_classes = (permissions.IsAuthenticated, )
