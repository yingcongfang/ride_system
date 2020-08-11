from django.db import models
from django.contrib.auth.models import User
# Create your models here.
        
class Ride(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=200, default='abc@gmail.com')

    dest = models.CharField(max_length=100, default='home')
    arrival = models.CharField(max_length=50, default="5:00pm-6:00pm")
    pnum = models.IntegerField(default='1')
    vtype = models.CharField(max_length=20, default='Sedan')
    child = models.BooleanField(default=False)#need a child seat or not
    share = models.BooleanField(default=False)#can this ride be shared or not
    
    status = models.CharField(max_length=20, default='Open')
    
    isOpen = models.BooleanField(default=True)
    isConfirmed = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    
    driver_id = models.IntegerField(default='0')
    #passenger_id = models.IntegerField(default='0')
    
    def __str__(self):
        return str(self.id)


       
class sharedRide(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=200, default='def@gmail.com')

    dest = models.CharField(max_length=100, default='bar')
    arrival = models.CharField(max_length=50, default="5:00pm-6:00pm")
    pnum = models.IntegerField(default='1')        
    
    def __str__(self):
        return str(self.id)