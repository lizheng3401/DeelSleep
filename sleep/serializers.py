from rest_framework import serializers
from device.models import Device
from account.models import User
from .models import Sleep


class SleepSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Sleep
        fields = "__all__"

