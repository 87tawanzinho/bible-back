from django.db import models

# Create your models here.

class TextsDevotional(models.Model):
    title = models.CharField(max_length=200) 
    content = models.TextField()
    version = models.CharField(max_length=10)
    concluded = models.BooleanField(default=False) 