from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas //

urlpatterns = patterns('',
	url(r'^$', Usuario),
	url(r'^privado/$', ingreso),
	url(r'^cerrar/$', serrar),
	url(r'^datos/(?P<id>\d+)/$',Datos),
	url(r'^editarperfil/$',editar_perfil),
	url(r'^nuevo/$',nuevoUser.as_view(), name='nuevoUser'),
)