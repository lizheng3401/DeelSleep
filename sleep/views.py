from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Sleep, Report
from api.models import SleepRecord
from .serializers import SleepSerializer, ReportSerializer


class SleepViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'device')

    def perform_create(self, serializer):
        new_sleep = serializer.save(user=self.request.user)
        SleepRecord(time=new_sleep.time_stamp, user=new_sleep.user, device=new_sleep.device, sleep=new_sleep).save()


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', )

    def perform_create(self, serializer):
        new_report = serializer.save(user=self.request.user)
        # sleep_record = SleepRecord.objects.get(sleep=new_report.sleep)
        # sleep_record.report = new_report
        # sleep_record.save()
