from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    firstCard = [
        {'id': 1, 'title': 'be a friend of jesus', 'completed': False}, 
        {'id': 2, 'title': 'knowing the word of god', 'completed': False},
        {'id': 3, 'title': 'jesus and his sheep','completed': False},
    ]

    firstCard = models.JSONField(default=firstCard, blank=True, null=True)

    def __str__(self): 
        return self.user.username
    
    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)