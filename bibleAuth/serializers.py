from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import Profile
class UserSerializer(serializers.ModelSerializer): 
    class Meta(object):
        model = User 
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'firstCard']