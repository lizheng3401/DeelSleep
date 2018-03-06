from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='device-detail')
    sleeps = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sleep-detail')

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