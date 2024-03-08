from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import Profile
class UserSerializer(serializers.ModelSerializer): 
    class Meta(object):
        model = User 
      
        exclude = ['password', 'last_login', 'is_active', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined', 'groups', 'user_permissions']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'allChapters', 'myBirds']


class UserWithoutChapter(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile 
        fields = ['user', 'devotionalWarn', 'myBirds']

