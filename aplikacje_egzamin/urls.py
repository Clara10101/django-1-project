from django.conf.urls import patterns, include, url
from pracownicy import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aplikacje_egzamin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pokazWszystko),
    url(r'^pracownik-([0-9]+)/$', views.pokazPracownika),
    url(r'^pracownicy/$', views.pokazPracownikow),
    url(r'^zespoly/$', views.pokazZespoly),
    url(r'^zespol-([0-9]+)/$', views.pokazZespol),
    url(r'^etaty/$', views.pokazEtaty),
    url(r'^etat-([0-9]+)/$', views.pokazEtat),
    url(r'^ajax/ajaxZapiszPlaca/', views.ajaxZapiszPlaca, name='zapis ajax'),
)