from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass
    
    def __str__(self):
        return self.username