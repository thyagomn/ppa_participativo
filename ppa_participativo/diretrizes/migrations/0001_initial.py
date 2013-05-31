# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Eixo'
        db.create_table(u'diretrizes_eixo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dt_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'diretrizes', ['Eixo'])

        # Adding model 'Area'
        db.create_table(u'diretrizes_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fk_eixo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diretrizes.Eixo'])),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dt_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'diretrizes', ['Area'])

        # Adding model 'Acao'
        db.create_table(u'diretrizes_acao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fk_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diretrizes.Area'])),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dt_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'diretrizes', ['Acao'])


    def backwards(self, orm):
        # Deleting model 'Eixo'
        db.delete_table(u'diretrizes_eixo')

        # Deleting model 'Area'
        db.delete_table(u'diretrizes_area')

        # Deleting model 'Acao'
        db.delete_table(u'diretrizes_acao')


    models = {
        u'diretrizes.acao': {
            'Meta': {'object_name': 'Acao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dt_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fk_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diretrizes.Area']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'diretrizes.area': {
            'Meta': {'object_name': 'Area'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dt_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fk_eixo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diretrizes.Eixo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'diretrizes.eixo': {
            'Meta': {'object_name': 'Eixo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dt_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['diretrizes']