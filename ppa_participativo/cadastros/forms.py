# coding: utf-8
from django import forms
from django.forms.widgets import TextInput, Select, DateInput
from ppa_participativo.core.funcoes import valida_cpf, valida_cnpj
from ppa_participativo.cadastros.models import Pessoa, Entidade, SEXO, ESCOLARIDADE


class DateField(forms.DateField):
    def clean(self, data):
        """
        Impede que o usuário insira uma data inválida
        """
        if data:
            dia, mes, ano = data.split('/')
            data = ano + "-" + mes + "-" + dia

            if data == '1900-01-01':
                raise forms.ValidationError('Digite uma data válida!')
        if data == "":
            raise forms.ValidationError('Este campo é obrigatório.')

        return data


class CPF(forms.CharField):
    def clean(self, cpf):
        if cpf:
            cpf = cpf.replace('.', '').replace('-', '')
            if not valida_cpf(cpf):
                raise forms.ValidationError('CPF inválido!')

        return cpf


class CNPJ(forms.CharField):
    def clean(self, cnpj):
        if cnpj:
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            if not valida_cnpj(cnpj):
                raise forms.ValidationError('CNPJ inválido!')

        return cnpj


class telefone(forms.CharField):
    def clean(self, fone):
        if fone:
            fone = fone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

        return fone


class PessoaForm(forms.ModelForm):
    nome = forms.CharField(label=u'Nome', widget=TextInput(attrs={'style': 'width: 96%'}))
    cpf = CPF(label=u'CPF', max_length=11, widget=TextInput(attrs={'style': 'width: 90%'}))
    dt_nascimento = DateField(label=u'Data Nasc.', widget=DateInput(attrs={'style': 'width: 90%'}))
    sexo = forms.ChoiceField(label=u'Sexo', choices=[('', '---------')]+SEXO, widget=Select(attrs={'style': 'width: 95%'}))
    escolaridade = forms.ChoiceField(label=u'Escolaridade', choices=[('', '---------')]+ESCOLARIDADE, widget=Select(attrs={'style': 'width: 98%'}))
    email = forms.EmailField(label=u'E-mail', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    telefone = forms.CharField(label=u'Telefone', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)

    class Meta:
        model = Pessoa


class EntidadeForm(forms.ModelForm):
    descricao = forms.CharField(label=u'Descrição', widget=TextInput(attrs={'style': 'width: 96%'}), required=False)
    cnpj = CNPJ(label=u'CNPJ', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    cargo = forms.CharField(label=u'Cargo', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    municipio = forms.CharField(label=u'Município', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    logradouro = forms.CharField(label=u'Logradouro', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    numero = forms.CharField(label=u'Número', max_length=5, widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    complemento = forms.CharField(label=u'Complemento', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    bairro = forms.CharField(label=u'Bairro', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    cep = forms.CharField(label=u'CEP', max_length=9, widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    email = forms.EmailField(label=u'Email', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)
    telefone = forms.CharField(label=u'Telefone', widget=TextInput(attrs={'style': 'width: 90%'}), required=False)

    class Meta:
        model = Entidade
