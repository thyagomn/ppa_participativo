#coding: utf-8
from django.contrib import admin
from ppa_participativo.eventos.models import Programacao, Reuniao


class ProgramacaoAdmin(admin.ModelAdmin):
    pass


class ReuniaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Programacao, ProgramacaoAdmin)
admin.site.register(Reuniao, ReuniaoAdmin)
