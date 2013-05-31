# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


def ppa(request):
    return render(request, 'ppa.html')
