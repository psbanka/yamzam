from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import logging

logger = logging.getLogger(__name__)


class EmailSummary(models.Model):
    """
    Keeps track of email imported from gmail
    credentials for logging into other cloud services.
    """
    user = models.ForeignKey(User, unique=False)
    message_id = models.BigIntegerField(blank=False, null=False)
    subject = models.CharField(max_length=150, blank=True, null=True)
    source_addr = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(blank=False, null=False)
    imported_to_wordpress = models.BooleanField(null=False)

    def __unicode__(self):
        return "%s/%s" % (self.id, self.source_addr)


class UserProfile(models.Model):
    """
    Keeps track of extra information about the user, specifically
    credentials for logging into other cloud services.
    """
    #user = models.ForeignKey(User, unique=True)
    user = models.OneToOneField(User)
    wp_url = models.CharField(max_length=200, blank=True, null=True)
    wp_username = models.CharField(max_length=50, blank=True, null=True)
    wp_password = models.CharField(max_length=100, blank=True, null=True)
    gmail_username = models.CharField(max_length=50, blank=True, null=True)
    gmail_password = models.CharField(max_length=100, blank=True, null=True)
    gmail_source = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    logger.info("in create_user_profile (%s)" % created)
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: u.get_profile())
