from django.db import models
from account.models import User


class Device(models.Model):
    nID = models.CharField(max_length=64)
    isActive = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name="devices", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nID

    class Meta:
        ordering = ('-created', )