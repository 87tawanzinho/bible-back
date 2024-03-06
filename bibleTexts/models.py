from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TextsDevotional(models.Model):
    title = models.CharField(max_length=200) 
    summary = models.CharField(max_length=400)
    content = models.TextField()
    version = models.CharField(max_length=10)
    chapter = models.CharField(max_length=30)
    concluded_by = models.ManyToManyField(User, related_name='concluded_devotionals')
