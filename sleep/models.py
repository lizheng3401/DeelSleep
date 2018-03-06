from django.db import models
from account.models import User
from device.models import Device


class Sleep(models.Model):
    time_stamp = models.DateField(auto_now_add=True)

    score = models.DecimalField(max_digits=3, decimal_places=1)
    move = models.IntegerField()
    breathe_stop = models.IntegerField(default=0)

    begin = models.DateTimeField()
    end = models.DateTimeField()
    N1 = models.DecimalField(max_digits=4, decimal_places=2)
    N2 = models.DecimalField(max_digits=4, decimal_places=2)
    N3 = models.DecimalField(max_digits=4, decimal_places=2)
    REM = models.DecimalField(max_digits=4, decimal_places=2)
    data = models.FileField(upload_to='sleepData/%Y/%m/%d')

    user = models.ForeignKey(User, related_name='sleeps')
    device = models.ForeignKey(Device, related_name='sleeps')

    def __str__(self):
        return self.time_stamp

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