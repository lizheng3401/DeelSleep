from rest_framework import serializers
from .models import Device
from sleep.models import Sleep


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    sleeps = serializers.HyperlinkedRelatedField(many=True, view_name="sleep-detail", read_only=True)

    class Meta:
        model = Device
        fields = ('nID', 'owner', 'isActive', 'sleeps')
