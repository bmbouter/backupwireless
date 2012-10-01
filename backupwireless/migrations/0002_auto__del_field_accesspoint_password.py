# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AccessPoint.password'
        db.delete_column('backupwireless_accesspoint', 'password')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'AccessPoint.password'
        raise RuntimeError("Cannot reverse this migration. 'AccessPoint.password' and its values cannot be restored.")

    models = {
        'backupwireless.accesspoint': {
            'Meta': {'object_name': 'AccessPoint'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'backupwireless.wirelessnetwork': {
            'Meta': {'object_name': 'WirelessNetwork'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['backupwireless']