from rest_framework import serializers

from .models import SleepRecord


class SleepRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SleepRecord
        fields = "__all__"
        # fields = ('createdTime', 'time', 'user', 'device', 'sleep', 'report')