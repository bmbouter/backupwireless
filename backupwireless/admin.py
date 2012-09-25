from django.contrib import admin

from backupwireless.models import WirelessNetwork, AccessPoint

admin.site.register(WirelessNetwork)
admin.site.register(AccessPoint)
