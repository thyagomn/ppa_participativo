#coding: utf-8
from django.contrib import admin
from ppa_participativo.votacoes.models import Voto
from django.conf import settings
import xmlrpclib

CLIENTE = xmlrpclib.ServerProxy(settings.WEBSERVICE_URL)  # cria cliente para o web service


class VotoInLine(admin.TabularInline):
    model = Voto
    extra = 0
    readonly_fields = ['eixo', 'area', 'fk_acao',  'voto_manual', 'bairro']
    fieldsets = ((None, {
        'fields': (( 'eixo', 'area', 'fk_acao', 'voto_manual', 'bairro'),),
    }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def eixo(self, obj):
        return obj.fk_acao.fk_area.descricao

    def area(self, obj):
        return obj.fk_acao.descricao

    def voto_manual(self, obj):
        return obj.voto or '-'
    voto_manual.short_description = u'Descricção do Voto'

    def bairro(self, obj):
        localizacao = CLIENTE.consultaBairro(obj.localizacao)
        print localizacao
        return localizacao[0]['codigo'] + ' / ' + localizacao[0]['descricao']
