# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

SEXO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]
ESCOLARIDADE = [("01", "Fundamental incompleto"), ("02", "Fundamental completo"),
                ("05", u"Médio incompleto"), ("04", u"Médio normal/Magistério"), ("06", u"Médio completo"),
                ("14", "Ensino Técnico"), ("07", "Superior incompleto"), ("08", "Superior Completo"),
                ("09", u"Pós-graduação"), ("10", "Mestrado"), ("11", "Doutorado"), ("12", u"Pós-dourado")]


class Pessoa(models.Model):
    cpf = models.CharField(_(u'CPF'), max_length=11, unique=True)
    nome = models.CharField(_(u'Nome'), max_length=200)
    dt_nascimento = models.DateField(_(u'Data Nasc.'))
    sexo = models.CharField(max_length=2, choices=SEXO)
    escolaridade = models.CharField(_(u'Escolaridade'), max_length=2, choices=ESCOLARIDADE)
    email = models.EmailField(_(u'Email'), blank=True, null=True)
    telefone = models.CharField(_(u'Telefone/Celular'), max_length=20, blank=True, null=True)
    dt_cadastro = models.DateTimeField(_(u'Data Cadastro'), auto_now_add=True)
    entidade = models.ForeignKey('cadastros.Entidade', blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'


class Entidade(models.Model):
    descricao = models.CharField(_(u'Entidade'), max_length=100, blank=True, null=True)
    cnpj = models.CharField(_(u'CPF'), max_length=14, blank=True, null=True)
    cargo = models.CharField(_(u'Cargo'), max_length=100, null=True)
    municipio = models.CharField(_(u'Município'), max_length=100, null=True)
    logradouro = models.CharField(_(u'Logradouro'), max_length=250, null=True)
    numero = models.CharField(_(u'Número'), max_length=5, null=True)
    complemento = models.CharField(_(u'Complemento'), max_length=250, null=True)
    bairro = models.CharField(_(u'Bairro'), max_length=50, null=True)
    cep = models.CharField(_(u'CEP'), max_length=8, null=True)
    email = models.EmailField(_(u'Email'), null=True)
    telefone = models.CharField(_(u'Telefone/Celular'), max_length=20, null=True)

    def __unicode__(self):
        return self.descricao

    class Meta:
        verbose_name = u'Entidade'
        verbose_name_plural = u'Entidades'
