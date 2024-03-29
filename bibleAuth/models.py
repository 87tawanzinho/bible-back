from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    allChapters = {
        'firstChapter': [
        {'id': 1, 'completed': False}, 
        {'id': 2, 'completed': False},
        {'id': 3, 'completed': False},
        {'id': 4, 'completed': False},
        ]
    }

    allChapters = models.JSONField(default=allChapters, blank=True, null=True)
    devotionalWarn = models.BooleanField(default=False) 

    myPrays = models.IntegerField(default=0)
    myBibles = models.IntegerField(default=0)
    

    def __str__(self): 
        return self.user.username
    
    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)