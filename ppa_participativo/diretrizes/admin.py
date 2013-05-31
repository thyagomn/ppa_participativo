#coding: utf-8
from django.contrib import admin
from ppa_participativo.diretrizes.models import Eixo, Area, Acao


class EixoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ativo',)
    list_filter = ['dt_cadastro', ]


class AreaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'fk_eixo', 'ativo',)
    list_filter = ['dt_cadastro', 'fk_eixo', ]


class AcaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'fk_area', 'ativo',)
    list_filter = ['dt_cadastro', 'fk_area', ]


admin.site.register(Eixo, EixoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Acao, AcaoAdmin)
