# coding: utf-8
from django.shortcuts import render
from django.db.models import Q
from ppa_participativo.eventos.models import Programacao
from datetime import time
import locale
import datetime


def programacao(request):
    locale.setlocale(locale.LC_ALL, '')
    filtro_data = {}
    meio_dia = time(12)
    fim_dia = time(18)
    print fim_dia
    programacao = Programacao.objects.filter(data__gte=datetime.date.today(), hora__gte=datetime.datetime.now().time()).order_by('data', 'hora')
    for mes in range(1, 13):

        if programacao.filter(Q(data__month=mes)).exists():
            filtro_dia = {}
            for dia in range(1, 32):
                # aux = []
                programa_dia = programacao.filter(Q(data__month=mes), Q(data__day=dia)).order_by('data', 'hora') if programacao.filter(Q(data__month=mes), Q(data__day=dia)).exists() else None
                if programa_dia:
                    periodos = {}
                    periodos['Manhã'] = []
                    periodos['Tarde'] = []
                    periodos['Noite'] = []
                    for programa in programa_dia:
                        if programa.hora < meio_dia:
                            periodos['Manhã'].append(programa)
                        elif programa.hora > fim_dia:
                            periodos['Noite'].append(programa)
                        else:
                            periodos['Tarde'].append(programa)
                    filtro_dia[dia] = periodos
            # print filtro_dia
            filtro_data[datetime.date(2013, mes, 01).strftime('%B').capitalize()] = filtro_dia
    print filtro_data
    return render(request, 'eventos/programacao.html', {'programacao': filtro_data})
