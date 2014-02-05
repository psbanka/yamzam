__author__ = 'bankap'

############################### EXPERIMENT USING DJANGO REST_FRAMEWORK


from django.http import HttpResponse
from django.contrib.auth.models import User
import models
from rest_framework import viewsets
import serializers
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class EmailSummaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmailSummaries to be viewed or edited.
    """
    queryset = models.EmailSummary.objects.all()
    serializer_class = serializers.EmailSummarySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
