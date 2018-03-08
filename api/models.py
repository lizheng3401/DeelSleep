from django.db import models
from sleep.models import Sleep, Report
from device.models import Device
from account.models import User


class SleepRecord(models.Model):

    createdTime = models.DateTimeField(auto_now_add=True)
    time = models.DateField()
    user = models.ForeignKey(User, related_name="UR", on_delete=models.CASCADE)
    device = models.ForeignKey(Device, related_name="DR", on_delete=models.CASCADE)
    sleep = models.ForeignKey(Sleep, related_name="SR", on_delete=models.CASCADE)
    # report = models.ForeignKey(Report, related_name="RR", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ("id", )

