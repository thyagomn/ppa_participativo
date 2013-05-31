# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Acao.acao_manual'
        db.add_column(u'diretrizes_acao', 'acao_manual',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Acao.acao_manual'
        db.delete_column(u'diretrizes_acao', 'acao_manual')


    models = {
        u'diretrizes.acao': {
            'Meta': {'object_name': 'Acao'},
            'acao_manual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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