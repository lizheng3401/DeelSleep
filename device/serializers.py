from rest_framework import serializers
from .models import Device
from sleep.models import Sleep


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    sleeps = serializers.PrimaryKeyRelatedField(many=True, queryset=Sleep.objects.all())

    class Meta:
        model = Device
        fields = ('nID', 'owner', 'isActive', 'sleeps')
