from rest_framework import serializers

from .models import User
from device.models import Device
from sleep.models import Sleep


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    sleeps = serializers.PrimaryKeyRelatedField(many=True, queryset=Sleep.objects.all())

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_superuser', 'devices', 'sleeps')