# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from ppa_participativo.cadastros.forms import PessoaForm, EntidadeForm
from ppa_participativo.cadastros.models import Pessoa
from ppa_participativo.core.funcoes import valida_cpf, mascara_cnpj
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from ppa_participativo.votacoes.models import Voto
import datetime


def cadastro(request):
    if request.method == 'POST':
        return salvar_cadastro(request)
    else:
        return novo_cadastro(request)


def novo_cadastro(request):
    return render(request, 'cadastros/cadastro_formulario.html', {'form_pessoa': PessoaForm(), 'form_entidade': EntidadeForm()})


def salvar_cadastro(request):
    formulario_pessoa = PessoaForm(request.POST)
    formulario_entidade = EntidadeForm(request.POST)

    if Pessoa.objects.filter(cpf=request.POST['cpf'].replace('.', '').replace('-', '')).exists():
        pessoa = Pessoa.objects.get(cpf=request.POST['cpf'].replace('.', '').replace('-', ''))
        qtd_votos = 10 - Voto.objects.filter(fk_pessoa=pessoa).count() if Voto.objects.filter(fk_pessoa=pessoa).exists() else 10

        if qtd_votos:
            return HttpResponseRedirect('/votacao/'+str(pessoa.pk)+'/')

    if not formulario_pessoa.is_valid() or not formulario_entidade.is_valid():
        return render(request, 'cadastros/cadastro_formulario.html', {'form_pessoa': formulario_pessoa, 'form_entidade': formulario_entidade})

    entidade = formulario_entidade.save() if formulario_entidade.cleaned_data['descricao'] and formulario_entidade.cleaned_data['cnpj'] else None
    pessoa = formulario_pessoa.save()

    if entidade:
        pessoa.entidade = entidade
        pessoa.save()

    return HttpResponseRedirect('/votacao/'+str(pessoa.pk)+'/')


@csrf_exempt
def verifica_cadastro(request):
    if request.is_ajax():
        cpf = request.POST['cpf'].replace('.', '').replace('-', '')
        if cpf and valida_cpf(cpf):
            if Pessoa.objects.filter(cpf=cpf).exists():
                pessoa_banco = Pessoa.objects.get(cpf=cpf)
                pessoa = {}

                for attr, value in pessoa_banco.__dict__.iteritems():
                    if type(value) is datetime.date:
                        pessoa[attr] = value.strftime("%d/%m/%Y")
                    elif not attr == '_state' and not attr == 'dt_cadastro':
                        pessoa[attr] = value or ''

                if pessoa_banco.entidade:
                    for attr, value in pessoa_banco.entidade.__dict__.iteritems():
                        if not attr == '_state':
                            pessoa[attr] = value or '' if attr != 'cnpj' else mascara_cnpj(value) or ''
                # print pessoa
                qtd_votos = 10 - Voto.objects.filter(fk_pessoa=pessoa_banco).count() if Voto.objects.filter(fk_pessoa=pessoa_banco).exists() else 10

                dados = {'existe_cpf': 'true',
                         'existe_erro': 'false',
                         'pessoa': pessoa,
                         'mensagem_erro': 'Você ainda possui <strong style="color: red">' + str(qtd_votos) + ' votos</strong> disponíveis.<br><br>Clique em <strong>votar</strong> para realizar a votação.' if qtd_votos else 'Este CPF já está cadastrado e não possui votos restantes.'}
            else:
                dados = {'existe_cpf': 'false', 'existe_erro': 'false', 'mensagem_erro': ''}
        else:
            dados = {'existe_cpf': 'false', 'existe_erro': 'true', 'mensagem_erro': 'CPF inválido! Verifique o CPF informado e tente novamente!'}

        return HttpResponse(simplejson.dumps(dados), mimetype="application/json")

    return HttpResponse(status=400)
