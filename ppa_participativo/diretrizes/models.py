# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Eixo(models.Model):
    descricao = models.CharField(_(u'Descrição'), max_length=200)
    ativo = models.BooleanField(_(u'Ativo'), default=True)
    dt_cadastro = models.DateTimeField(_(u'Data Cadastro'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.descricao)

    class Meta:
        verbose_name = u'Eixo'
        verbose_name_plural = u'Eixos'


class Area(models.Model):
    fk_eixo = models.ForeignKey(Eixo, verbose_name=u'Eixo')
    descricao = models.CharField(_(u'Descrição'), max_length=200)
    ativo = models.BooleanField(_(u'Ativo'), default=True)
    dt_cadastro = models.DateTimeField(_(u'Data Cadastro'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.descricao)

    def acoes(self):
        return Acao.objects.filter(fk_area=self, ativo=True).order_by('acao_manual', 'descricao') if Acao.objects.filter(fk_area=self, ativo=True).exists() else None

    class Meta:
        verbose_name = u'Área'
        verbose_name_plural = u'Áreas'


class Acao(models.Model):
    fk_area = models.ForeignKey(Area, verbose_name=u'Area')
    descricao = models.CharField(_(u'Descrição'), max_length=200)
    ativo = models.BooleanField(_(u'Ativo'), default=True)
    acao_manual = models.BooleanField(_(u'Informado pelo cidadão'), default=False)
    dt_cadastro = models.DateTimeField(_(u'Data Cadastro'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.descricao)

    class Meta:
        verbose_name = u'Ação'
        verbose_name_plural = u'Ações'
