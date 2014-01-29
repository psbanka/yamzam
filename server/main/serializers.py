__author__ = 'bankap'

from django.contrib.auth.models import User
from models import UserProfile


from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """
    A serializer for .
    """
    class Meta(object):
        model = User


class UserProfileSerializer(ModelSerializer):
    """
    A serializer for .
    """
    class Meta(object):
        model = UserProfile
