from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickName = models.CharField(max_length=50,blank=True)
    class Meta(AbstractUser.Meta):
        pass
    
    def __str__(self):
        return self.nickName