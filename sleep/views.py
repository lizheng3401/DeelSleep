from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Sleep
from .serializers import SleepSerializer
# Create your views here.


class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'device')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)