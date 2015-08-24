from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas

urlpatterns = patterns('',
	#url(r'^$',index.as_view()),
	url(r'^AvisosDenuncias/$',AvisosDenuncias.as_view(),name='AvisosDenuncias'),
	url(r'^AvisosNotificaciones/$',AvisosNotificaciones.as_view(),name='AvisosNotificaciones'),
	url(r'^EnviarNotificacion/$',EnviarNotificacion, name='EnviarNotificacion'),
	url(r'^Notiicaciones/(?P<id>\d+)/$',Notiicaciones, name='Notiicaciones'),
	url(r'^Cronograma/$',RegistroCronograma, name='RegistroCronograma'),

	url(r'^datosDenuncia/(?P<id>\d+)/$',datosDenuncia, name='datosDenuncia'),
	url(r'^detDenuncias/(?P<id>\d+)/$',detDenuncias, name='detDenuncias'),
	url(r'^DetalleDenuncias/(?P<id>\d+)/$',DetalleDenuncias, name='DetalleDenuncias'),
	url(r'^VerNotificacionesInspector/(?P<id>\d+)/$',VerNotificacionesInspector, name='VerNotificacionesInspector'),
	url(r'^TodaslasNotificaciones/$',TodaslasNotificaciones, name='TodaslasNotificaciones'),
	url(r'^TodaslasDenuncias/$',TodaslasDenuncias, name='TodaslasDenuncias'),
	url(r'^ConsultarDenunciaFecha/$',ConsultarDenunciaFecha.as_view(), name='ConsultarDenunciaFecha'),
	url(r'^ConsultarDenunciaClienteFecha/$',ConsultarDenunciaClienteFecha.as_view(), name='ConsultarDenunciaClienteFecha'),
)