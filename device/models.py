from django.db import models
from account.models import User
# Create your models here.

class Device(models.Model):
    nID = models.CharField(max_length=64)
    isActive = models.BooleanField(default=False)
    owner =  models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.ID