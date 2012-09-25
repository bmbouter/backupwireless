# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WirelessNetwork'
        db.create_table('backupwireless_wirelessnetwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('online', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('backupwireless', ['WirelessNetwork'])

        # Adding model 'AccessPoint'
        db.create_table('backupwireless_accesspoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('backupwireless', ['AccessPoint'])


    def backwards(self, orm):
        # Deleting model 'WirelessNetwork'
        db.delete_table('backupwireless_wirelessnetwork')

        # Deleting model 'AccessPoint'
        db.delete_table('backupwireless_accesspoint')


    models = {
        'backupwireless.accesspoint': {
            'Meta': {'object_name': 'AccessPoint'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'backupwireless.wirelessnetwork': {
            'Meta': {'object_name': 'WirelessNetwork'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['backupwireless']