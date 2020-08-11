from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Ride

#@receiver(post_save, sender=User)
#def create_ride(sender, instance, created, **kwargs):
#  if created:
#    Ride.objects.create(user=instance)
#    
#@receiver(post_save, sender=User)
#def save_ride(sender, instance, **kwargs):
#  instance.profile.save()