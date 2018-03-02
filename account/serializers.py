from rest_framework import serializers

from .models import User
from device.models import Device


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'devices')