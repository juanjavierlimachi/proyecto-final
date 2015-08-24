from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas //

urlpatterns = patterns('',
	url(r'^denuncias/$', denucias.as_view()),
	url(r'^crear-comentario$', create_comment, name='crear-comentario'),
	url(r'^cliente/$', clienteView.as_view()),
	
)