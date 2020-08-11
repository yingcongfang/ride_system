from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  isdriver = models.BooleanField(default=0)
  license = models.CharField(default='NA',max_length=100)
  vehicle_type = models.CharField(default='NA',max_length=100)
  pnum = models.IntegerField(default=1)
  child = models.BooleanField(default=0)
  
  def __str__(self):
    return f'{self.user.username} Profile'