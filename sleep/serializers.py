from rest_framework import serializers

from device.models import Device
from account.models import User
from .models import Sleep, Report


class SleepSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())

    class Meta:
        model = Sleep
        fields = "__all__"


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    sleep = serializers.PrimaryKeyRelatedField(queryset=Sleep.objects.all())
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Report
        fields = "__all__"

