from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DeviceSerializer
from .models import Device
# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    