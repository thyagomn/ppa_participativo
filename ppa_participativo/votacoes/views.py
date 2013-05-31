# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from ppa_participativo.votacoes.models import Voto
from ppa_participativo.cadastros.models import Pessoa
from ppa_participativo.diretrizes.models import Area, Acao
from ppa_participativo.votacoes.forms import VotoForm
from django.forms.formsets import formset_factory


def votacao(request, contribuinte):
    if request.method == 'POST':
        return gravar_votacao(request, contribuinte)
        # return salvar_cadastro(request)
    else:
        return nova_votacao(request, contribuinte)


def gravar_votacao(request, contribuinte):
    formset_votos = formset_factory(VotoForm)
    formset = formset_votos(request.POST, request.FILES)
    if formset.is_valid():
        for form in formset:
            if 'voto' in form.cleaned_data and form.cleaned_data['voto'] and not Voto.objects.filter(fk_acao__pk=form.cleaned_data['acao'], fk_pessoa__pk=contribuinte).exists():
                if 'voto_manual'in form.cleaned_data:
                    voto = Voto(fk_acao=Acao.objects.get(pk=form.cleaned_data['acao']),
                                fk_pessoa=Pessoa.objects.get(pk=contribuinte),
                                voto=form.cleaned_data['descricao'],
                                localizacao=form.cleaned_data['localizacao'],)
                else:
                    voto = Voto(fk_acao=Acao.objects.get(pk=form.cleaned_data['acao']),
                                fk_pessoa=Pessoa.objects.get(pk=contribuinte),
                                localizacao=form.cleaned_data['localizacao'],)
                voto.save()
        return render(request, 'votacoes/votacoes_fim.html')
    pessoa = Pessoa.objects.get(pk=contribuinte)
    qtd_votos = 10 - Voto.objects.filter(fk_pessoa=pessoa).count() if Voto.objects.filter(fk_pessoa=pessoa).exists() else 10
    print formset[1].data
    return render(request, 'votacoes/votacao.html', {'areas': lista_areas(), 'pessoa': pessoa, 'qtd_votos': qtd_votos, 'form_votos': formset})


def nova_votacao(request, contribuinte):
    pessoa = Pessoa.objects.get(pk=contribuinte)
    qtd_votos = 10 - Voto.objects.filter(fk_pessoa=pessoa).count() if Voto.objects.filter(fk_pessoa=pessoa).exists() else 10
    lista_votos = [voto.fk_acao.pk for voto in Voto.objects.filter(fk_pessoa=pessoa)] if Voto.objects.filter(fk_pessoa=pessoa).exists() else []

    areas = lista_areas()
    lista = []
    if areas:
        for area in areas:
            acoes = area.acoes()
            for acao in acoes:
                if acao.pk in lista_votos:
                    voto = Voto.objects.get(fk_pessoa=pessoa, fk_acao=acao)
                    lista.append({'voto': 'checked', 'descricao': voto.voto, 'localizacao': voto.localizacao, 'acao': acao.pk, 'voto_manual': acao.acao_manual})
                else:
                    lista.append({'acao': acao.pk, 'voto_manual': acao.acao_manual})
    formset_votos = formset_factory(VotoForm, extra=0, max_num=len(lista))
    formset = formset_votos(initial=lista)

    return render(request, 'votacoes/votacao.html', {'areas': areas, 'pessoa': pessoa, 'qtd_votos': qtd_votos, 'form_votos': formset})


def lista_areas():
    # if Acao.objects.filter(ativo=True, fk_area__ativo=True, fk_area__fk_eixo__ativo=True).exists():
    #     lista_votos = [voto.fk_acao.pk for voto in Voto.objects.filter(fk_pessoa=pessoa)] if Voto.objects.filter(fk_pessoa=pessoa).exists() else []
    #     acoes = Acao.objects.filter(ativo=True, fk_area__ativo=True, fk_area__fk_eixo__ativo=True).exclude(pk__in=lista_votos)
    # else:
    #     acoes = None

    # if Area.objects.filter(pk__in=[acao.fk_area.pk for acao in acoes.distinct('fk_area')], ativo=True, fk_eixo__ativo=True).exists():
    if Area.objects.filter(ativo=True, fk_eixo__ativo=True, acao__ativo=True).exists():
        return Area.objects.filter(ativo=True, fk_eixo__ativo=True, acao__ativo=True).distinct().order_by('descricao')
    return None
