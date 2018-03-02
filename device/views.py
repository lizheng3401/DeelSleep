from rest_framework import viewsets,permissions
from .serializers import DeviceSerializer
from .models import Device
from utils.permissions import IsOwnerOrReadOnly


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)