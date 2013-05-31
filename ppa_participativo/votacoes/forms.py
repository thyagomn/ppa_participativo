# coding: utf-8
from django import forms
from ppa_participativo.votacoes.models import Voto
from django.conf import settings
import xmlrpclib

CLIENTE = xmlrpclib.ServerProxy(settings.WEBSERVICE_URL)  # cria cliente para o web service


class VotoForm(forms.Form):
    voto = forms.BooleanField(label='Votar', required=False)
    descricao = forms.CharField(label='Descição', max_length=75, required=False)
    localizacao = forms.ChoiceField(label=u'Localização', choices=[('', '-----------')]+CLIENTE.consultaBairros(), required=False)
    acao = forms.CharField(widget=forms.HiddenInput(), required=False)
    voto_manual = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = super(VotoForm, self).clean()
        voto = cleaned_data.get("voto")
        localizacao = cleaned_data.get("localizacao")
        voto_manual = cleaned_data.get("voto_manual")
        descricao = cleaned_data.get("descricao")

        if voto and not localizacao:
            # We know these are not in self._errors now (see discussion
            # below).
            self._errors["localizacao"] = self.error_class([u'Ao marcar votar, selecione uma localização.'])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            del cleaned_data["localizacao"]

        if voto and voto_manual and not descricao:
            # We know these are not in self._errors now (see discussion
            # below).
            self._errors["descricao"] = self.error_class([u'Ao votar manualmente, descreva a ação desejada.'])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            del cleaned_data["descricao"]

        # Always return the full collection of cleaned data.
        return cleaned_data
