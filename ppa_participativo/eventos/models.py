# -*- coding:utf-8 -*-
from django.db import models


class Evento(models.Model):
    atividade = models.CharField('Atividade', max_length=200)
    data = models.DateField('Data')
    hora = models.TimeField('Hora')
    local = models.CharField('Local', max_length=100)


class Reuniao(Evento):
    pass

    def __unicode__(self):
        return "%s - %s" % (self.atividade, str(self.data.strftime('%d/%m/%Y')))

    class Meta:
        verbose_name = u'Reunião'
        verbose_name_plural = u'Reuniões'


class Programacao(Evento):
    finalidade = models.CharField('Finalidade', max_length=200)

    def __unicode__(self):
        return "%s - %s - %s" % (self.atividade, self.finalidade, str(self.data.strftime('%d/%m/%Y')))

    class Meta:
        verbose_name = u'Programação'
        verbose_name_plural = u'Programações'
