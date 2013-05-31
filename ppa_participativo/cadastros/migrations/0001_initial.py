# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pessoa'
        db.create_table(u'cadastros_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dt_nascimento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('escolaridade', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dt_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('entidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cadastros.Entidade'], null=True, blank=True)),
        ))
        db.send_create_signal(u'cadastros', ['Pessoa'])

        # Adding model 'Entidade'
        db.create_table(u'cadastros_entidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=5, null=True)),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'cadastros', ['Entidade'])


    def backwards(self, orm):
        # Deleting model 'Pessoa'
        db.delete_table(u'cadastros_pessoa')

        # Deleting model 'Entidade'
        db.delete_table(u'cadastros_entidade')


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
        }
    }

    complete_apps = ['cadastros']