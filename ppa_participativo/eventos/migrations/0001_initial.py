# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evento'
        db.create_table(u'eventos_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atividade', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('hora', self.gf('django.db.models.fields.TimeField')()),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'eventos', ['Evento'])

        # Adding model 'Reuniao'
        db.create_table(u'eventos_reuniao', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['eventos.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'eventos', ['Reuniao'])

        # Adding model 'Programacao'
        db.create_table(u'eventos_programacao', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['eventos.Evento'], unique=True, primary_key=True)),
            ('finalidade', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'eventos', ['Programacao'])


    def backwards(self, orm):
        # Deleting model 'Evento'
        db.delete_table(u'eventos_evento')

        # Deleting model 'Reuniao'
        db.delete_table(u'eventos_reuniao')

        # Deleting model 'Programacao'
        db.delete_table(u'eventos_programacao')


    models = {
        u'eventos.evento': {
            'Meta': {'object_name': 'Evento'},
            'atividade': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'eventos.programacao': {
            'Meta': {'object_name': 'Programacao', '_ormbases': [u'eventos.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['eventos.Evento']", 'unique': 'True', 'primary_key': 'True'}),
            'finalidade': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'eventos.reuniao': {
            'Meta': {'object_name': 'Reuniao', '_ormbases': [u'eventos.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['eventos.Evento']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['eventos']