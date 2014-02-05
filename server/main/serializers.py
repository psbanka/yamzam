__author__ = 'bankap'

from django.contrib.auth.models import User
from models import UserProfile, EmailSummary


from rest_framework.serializers import ModelSerializer


class EmailSummarySerializer(ModelSerializer):
    """
    A serializer for EmailSummary.
    """
    class Meta(object):
        model = EmailSummary


class UserSerializer(ModelSerializer):
    """
    A serializer for Users.
    """
    class Meta(object):
        model = User


class UserProfileSerializer(ModelSerializer):
    """
    A serializer for UserProfiles.
    """
    class Meta(object):
        model = UserProfile
