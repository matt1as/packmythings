# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('web_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('web', ['Item'])

        # Adding model 'TypeOfTrip'
        db.create_table('web_typeoftrip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('web', ['TypeOfTrip'])

        # Adding model 'Trip'
        db.create_table('web_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('type_of_trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.TypeOfTrip'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=400)),
        ))
        db.send_create_signal('web', ['Trip'])

        # Adding model 'TripItemRelationship'
        db.create_table('web_tripitemrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Item'])),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Trip'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('packed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('web', ['TripItemRelationship'])

        # Adding model 'ItemTypeOfTripRelationship'
        db.create_table('web_itemtypeoftriprelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('counter', self.gf('django.db.models.fields.IntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Item'])),
            ('type_of_trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.TypeOfTrip'])),
        ))
        db.send_create_signal('web', ['ItemTypeOfTripRelationship'])

        # Adding model 'Page'
        db.create_table('web_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('web', ['Page'])

        # Adding model 'Text'
        db.create_table('web_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=800)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Page'])),
        ))
        db.send_create_signal('web', ['Text'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('web_item')

        # Deleting model 'TypeOfTrip'
        db.delete_table('web_typeoftrip')

        # Deleting model 'Trip'
        db.delete_table('web_trip')

        # Deleting model 'TripItemRelationship'
        db.delete_table('web_tripitemrelationship')

        # Deleting model 'ItemTypeOfTripRelationship'
        db.delete_table('web_itemtypeoftriprelationship')

        # Deleting model 'Page'
        db.delete_table('web_page')

        # Deleting model 'Text'
        db.delete_table('web_text')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.itemtypeoftriprelationship': {
            'Meta': {'object_name': 'ItemTypeOfTripRelationship'},
            'counter': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Item']"}),
            'type_of_trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.TypeOfTrip']"})
        },
        'web.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.text': {
            'Meta': {'object_name': 'Text'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '800'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Page']"})
        },
        'web.trip': {
            'Meta': {'object_name': 'Trip'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['web.Item']", 'null': 'True', 'through': "orm['web.TripItemRelationship']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'type_of_trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.TypeOfTrip']"})
        },
        'web.tripitemrelationship': {
            'Meta': {'object_name': 'TripItemRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Item']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'packed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Trip']"})
        },
        'web.typeoftrip': {
            'Meta': {'object_name': 'TypeOfTrip'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['web.Item']", 'null': 'True', 'through': "orm['web.ItemTypeOfTripRelationship']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']