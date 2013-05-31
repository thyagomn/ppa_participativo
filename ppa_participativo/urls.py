from django.conf.urls import patterns, include, url
from ppa_participativo.core.views import HomePageView
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^ppa/$', 'ppa_participativo.core.views.ppa', name='ppa'),
    url(r'^cadastro/$', 'ppa_participativo.cadastros.views.cadastro', name='cadastro'),
    url(r'^programacao/$', 'ppa_participativo.eventos.views.programacao', name='programacao'),
    url(r'^votacao/(?P<contribuinte>\d+)/$', 'ppa_participativo.votacoes.views.votacao', name='votacao'),
    url(r'^verificar_cadastro/$', 'ppa_participativo.cadastros.views.verifica_cadastro', name='verificar_cadastro'),
    # Examples:

    # url(r'^$', 'ppa_participativo.views.home', name='home'),
    # url(r'^ppa_participativo/', include('ppa_participativo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
