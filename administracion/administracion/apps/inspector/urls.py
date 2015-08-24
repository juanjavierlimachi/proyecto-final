from django.conf.urls import patterns, include, url
from .views import *
#from .views import denucias#aki ay estoy importando todas las mis vistas //

urlpatterns = patterns('',
	#url(r'^denuncias/$', denucias.as_view()), denuncias
	url(r'^buscarNegocio/$', buscarNegocio, name='buscarNegocio'),
	url(r'^emitirInfraccion/$', emitirInfraccion.as_view()),
	#url(r'^denuncias/$',denuncias.as_view(),name='denuncias'), AvisosDenunciasCliente
	url(r'^crear-notificacion$',crear_notificacion, name='crear_notificacion'),

	url(r'^Denuncias-cliente/$', AvisosDenunciasCliente.as_view()),
	url(r'^perfil/(?P<id>\d+)/$',perfilinspector),
	url(r'^DetalleNegocio/(?P<id>\d+)/$',DetalleNegocio),

	url(r'^VerDenunciasInspector/(?P<id>\d+)/$',VerDenunciasInspector),
	url(r'^EditarNotificacion/(?P<id>\d+)/$',EditarNotificacion),
	
	url(r'^datosDenunciaInspector/(?P<id>\d+)/$',datosDenuncia),
	url(r'^detaDenuncias/(?P<id>\d+)/$',detaDenuncias), 
)