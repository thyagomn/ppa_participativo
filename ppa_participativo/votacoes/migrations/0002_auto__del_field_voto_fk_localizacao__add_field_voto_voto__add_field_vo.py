# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Voto.fk_localizacao'
        db.delete_column(u'votacoes_voto', 'fk_localizacao')

        # Adding field 'Voto.voto'
        db.add_column(u'votacoes_voto', 'voto',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Voto.localizacao'
        db.add_column(u'votacoes_voto', 'localizacao',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Voto.fk_localizacao'
        db.add_column(u'votacoes_voto', 'fk_localizacao',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Voto.voto'
        db.delete_column(u'votacoes_voto', 'voto')

        # Deleting field 'Voto.localizacao'
        db.delete_column(u'votacoes_voto', 'localizacao')


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
        },
        u'votacoes.voto': {
            'Meta': {'object_name': 'Voto'},
            'fk_acao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diretrizes.Acao']", 'null': 'True', 'blank': 'True'}),
            'fk_pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cadastros.Pessoa']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localizacao': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'voto': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['votacoes']