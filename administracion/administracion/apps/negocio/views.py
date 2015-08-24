from django.shortcuts import render, render_to_response
from django.views.generic import CreateView,TemplateView,ListView
from .models import *
from administracion.apps.cliente.models import Comment
from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.db.models import Q
from django.template import RequestContext
from django.http import  HttpResponseRedirect, HttpResponse
# Create your views here.
def RegistroNegocio(request):
	if request.method=='POST':
		formulario=formNegocio(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/ListaNegocio/')
	else:
		formulario=formNegocio()
	return render_to_response('negocio/registroNegocio.html',{'formulario':formulario},context_instance=RequestContext(request))
def ListaNegocio(request):
    categorias=Categoria.objects.all().order_by('categoria')
    negosios=Negocio.objects.all().order_by('propietario')
    return render_to_response('negocio/ListaNegocio.html',{'categorias':categorias,'negosios':negosios},context_instance=RequestContext(request))

from django.core import serializers
class busquedaAjaxView(TemplateView):
    def get(self, request, *args, **kwargs):
        id_categoria = request.GET['id']
        elecion = Negocio.objects.filter(categoria=id_categoria).order_by('propietario')
        print elecion
        data = serializers.serialize('json', elecion,fields=('id','propietario','memorial_apertura'))
        return HttpResponse(data, 'application/json')
"""def buscar(request):
	if request.method=='POST':
		formulario=buscarForm(request.POST)
		if (formulario.is_valid()):
			criterio=request.POST["buscar"]
			if criterio!="":
				listas=Negocio.objects.filter(Q(propietario__contains=criterio) or Q(memorial_apertura__contains=criterio))
				return render_to_response('negocio/resultadoBus.html',{'listas':listas},RequestContext(request))
			else:
				HttpResponse("error")
	formulario=buscarForm()
	return render_to_response('negocio/formBusqueda.html',{'formulario':formulario},RequestContext(request))
""" 
def buscar(request):
    if request.method=="POST":
    	texto=request.POST['texto']
    	dato=int(texto)
    	negocios=Negocio.objects.all()
    	cont=0
    	negocio=[]
    	for i in negocios:
    		if dato==i.id:
    			cont=1
    			negocio=Negocio.objects.get(id=int(texto))
    	#acceso.is_active and acceso.is_superuser and acceso.is_staff:
        		return render_to_response('negocio/resultadoBus.html',{'negocio':negocio},context_instance=RequestContext(request))
        		break
        if cont==0:
        	return HttpResponse('No existe')
    else:
        texto=request.GET["texto"]
        busqueda=(
            Q(propietario__icontains=texto) |
            Q(propietario__icontains=texto) |
            Q(propietario__icontains=texto)
        )
        resultados=Negocio.objects.filter(busqueda).distinct()
        html="<ul class='ul_lista'>"
        for i in resultados:
            html=html+"<li><a href='/detalleNegocio/"+str(i.id)+"/'>"+i.propietario+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)

def DetallesNegocioBus(request,id):
    negocio=Negocio.objects.get(id=id)
    return render_to_response('negocio/resultadoBus.html',{'negocio':negocio},context_instance=RequestContext(request))


def registros(request,id):
	quejas=Comment.objects.filter(idNegocio=int(id)).order_by("-id")[0:30]
	return render_to_response('negocio/quejas.html',{'quejas':quejas},context_instance=RequestContext(request))
