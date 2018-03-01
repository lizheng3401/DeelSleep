from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Device
        fields = ('nID', 'owner', 'isActive')
