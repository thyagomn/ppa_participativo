#coding: utf-8
from django.contrib import admin
from ppa_participativo.cadastros.models import Pessoa, Entidade
from ppa_participativo.votacoes.admin import VotoInLine


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'dt_nascimento', 'sexo', 'escolaridade', 'dt_cadastro')
    inlines = [VotoInLine, ]


class EntidadeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Entidade, EntidadeAdmin)
