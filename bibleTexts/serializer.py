from rest_framework import serializers 
from .models import TextsDevotional 

class TextSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = TextsDevotional
        fields = '__all__'

    