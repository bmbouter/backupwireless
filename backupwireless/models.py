from django.db import models
from django.utils.translation import ugettext as _

class WirelessNetwork(models.Model):
	online = models.BooleanField(_(u"Online"), blank=False)

class AccessPoint(models.Model):
	ip = models.CharField(_(u"IP Address"), blank=False, max_length=16)
	username = models.CharField(_(u"Username"), blank=False, max_length=20)
	password = models.CharField(_(u"Password"), blank=False, max_length=20)
