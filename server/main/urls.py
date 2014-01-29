from django.conf.urls import url, patterns, include
from rest_framework import routers
from main import views
from django.contrib.auth.views import login
from main import serializer_views
from django.contrib import admin
admin.autodiscover()


## ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    model = User
#

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', serializer_views.UserViewSet)
router.register(r'userprofiles', serializer_views.UserProfileViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns(
    '',

    # HOOKS INTO ANGULAR #######################
    url(r'^$', views.index, name='index'),
    url(r'^partials/(?P<template_name>.*)', views.partial_helper),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),

    # DJANGO ADMINISTRATION ####################
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Django authorization calls
    url(r'^login/$', login, {'template_name': 'auth.html'}),
    url(r'^logout/$', views.logout_view),
)
#
#
#
#
#
#from django.conf.urls import patterns, url, include
#from main import serializer_views
#from rest_framework import routers
#
## Uncomment the next two lines to enable the admin:
#
#
#router = routers.DefaultRouter()
#router.register(r'users', serializer_views.UserViewSet)
#urlpatterns = patterns(
#    '',
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include(
#        'rest_framework.urls', namespace='rest_framework'))
#)

print router.urls
#urlpatterns += patterns(
#    '',
#
#    # RESTFUL CALLS ############################
#    url(r'^api/', include(router.urls)),
#    url(r'^api/current_user$', views.current_user, name="current_user"),
#
#
#    url(r'^contact$', views.contact, name='contact'),
#    url(r'^api-auth/', include('rest_framework.urls',
#                               namespace='rest_framework')),
#)
