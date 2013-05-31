#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import xmlrpclib

CLIENTE = xmlrpclib.ServerProxy(settings.WEBSERVICE_URL)  # cria cliente para o web service


class Voto(models.Model):
    voto = models.CharField('Voto', max_length=75, blank=True, null=True)
    fk_acao = models.ForeignKey('diretrizes.Acao', verbose_name=u'Ação', blank=True, null=True)
    fk_pessoa = models.ForeignKey('cadastros.Pessoa', verbose_name=u'Pessoa', blank=True, null=True)
    localizacao = models.CharField(_(u'Localização'), max_length=10, choices=CLIENTE.consultaBairros(), blank=True, null=True)

    def __unicode__(self):
        return u"%s: %s" % (self.fk_pessoa, self.fk_acao)

    class Meta:
        verbose_name = u'Voto'
        verbose_name_plural = u'Votos'
