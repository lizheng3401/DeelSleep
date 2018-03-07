from django.db import models
from account.models import User
from device.models import Device


class Sleep(models.Model):
    time_stamp = models.DateField(auto_now_add=True)

    score = models.FloatField()
    move = models.IntegerField()
    breathe_stop = models.IntegerField(default=0)

    begin = models.DateTimeField()
    end = models.DateTimeField()
    N1 = models.FloatField()
    N2 = models.FloatField()
    N3 = models.FloatField()
    REM = models.FloatField()
    data = models.FileField(upload_to='sleepData/%Y/%m/%d')

    user = models.ForeignKey(User, related_name='sleeps')
    device = models.ForeignKey(Device, related_name='sleeps')

    def __str__(self):
        return str(self.time_stamp)

    class Meta:
        ordering = ("time_stamp", )


class Report(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    sleep = models.ForeignKey(Sleep, related_name='reports')
    user = models.ForeignKey(User, related_name='reports')

    def __str__(self):
        return self.user

    class Meta:
        ordering = ('-created_time', )