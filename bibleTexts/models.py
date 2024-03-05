from django.db import models

# Create your models here.

class TextsDevotional(models.Model):
    title = models.CharField(max_length=200) 
    summary = models.CharField(max_length=400)
    content = models.TextField()
    version = models.CharField(max_length=10)
    chapter = models.CharField(max_length=30)
    concluded = models.BooleanField(default=False) 