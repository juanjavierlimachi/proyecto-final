from django.conf.urls import patterns, include, url
from django.contrib import admin
#from administracion.apps.cliente.views import create_comment
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'administracion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
        #las urls de mi aplicacion inicio
    url(r'^',include('administracion.apps.inicio.urls')),
    #las urls de mi aplicacion usuario
    url(r'^',include('administracion.apps.usuario.urls')),
    #las urls de mi aplicacion secretaria
    url(r'^',include('administracion.apps.secretaria.urls')),
    #las urls de mi aplicacion cliente
    url(r'^',include('administracion.apps.cliente.urls')),
    #las urls de mi aplicacion inspector 
    url(r'^',include('administracion.apps.inspector.urls')),
    #las urls de mi aplicacion negocio
    url(r'^',include('administracion.apps.negocio.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),
)
