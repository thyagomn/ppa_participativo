# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voto'
        db.create_table(u'votacoes_voto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fk_acao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diretrizes.Acao'], null=True, blank=True)),
            ('fk_pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastros.Pessoa'], null=True, blank=True)),
            ('fk_localizacao', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'votacoes', ['Voto'])


    def backwards(self, orm):
        # Deleting model 'Voto'
        db.delete_table(u'votacoes_voto')


    models = {
        u'cadastros.entidade': {
            'Meta': {'object_name': 'Entidade'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'cadastros.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'dt_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dt_nascimento': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'entidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cadastros.Entidade']", 'null': 'True', 'blank': 'True'}),
            'escolaridade': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
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
        },
        u'votacoes.voto': {
            'Meta': {'object_name': 'Voto'},
            'fk_acao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diretrizes.Acao']", 'null': 'True', 'blank': 'True'}),
            'fk_localizacao': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'fk_pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cadastros.Pessoa']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['votacoes']