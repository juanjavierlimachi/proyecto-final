from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from administracion.apps.negocio.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from administracion.apps.negocio.models import multa
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import User
from administracion.apps.usuario.models import Perfiles
from .forms import *
from django.db.models import Q
from administracion.apps.negocio.models import Negocio
from administracion.apps.cliente.models import *
from administracion.apps.cliente.forms import *
# Create your views here.
def perfilinspector(request,id):
	perfil=User.objects.filter(id=id)
	dato=Perfiles.objects.all()
	return render_to_response('inspector/perfil.html',{'perfil':perfil,'dato':dato},context_instance=RequestContext(request))

def buscarNegocio(request):
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
        		return render_to_response('inspector/resultadoBusNegocio.html',{'negocio':negocio},context_instance=RequestContext(request))
        		break
        if cont==0:
        	return HttpResponse('No existe')
    else:
        texto=request.GET["texto"]
        print texto
        busqueda=(
            Q(propietario__icontains=texto) |
            Q(propietario__icontains=texto) |
            Q(propietario__icontains=texto)
        )
        datos=Negocio.objects.filter(busqueda).distinct()
        html="<ul class='ul_lista'>"
        for i in datos:
            html=html+"<li><a href='/DetalleNegocio/"+str(i.id)+"/'>"+i.propietario+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)

def DetalleNegocio(request, id):
	negocio=Negocio.objects.get(id=id)
	return render_to_response('inspector/resultadoBusNegocio.html',{'negocio':negocio},context_instance=RequestContext(request))

class emitirInfraccion(TemplateView):
	def get(self, request, *args, **kwargs):
		contexto=request.user
		multas=multa.objects.all().order_by("-id")[0:3]
		dic = {
			'user':contexto,
			'form': FormMulta(),
			'multa':multas
		}
			#una ves optenido el nombre enviamos al templete cliente.html
		return render(request, 'inspector/formMultas.html', dic)
		
	def post(self, request, *args, **kwargs):
		#print 'isiste un POST'
		multa.objects.create(
				idUser = request.POST['idUser'],
				Usuario = request.POST['Usuario'],
				descripcion = request.POST['descripcion'],
				Codigo = request.POST['Codigo'],
				fecha_presentacion=request.POST['fecha_presentacion'],
				hora = request.POST['hora']
			)
		#aki redirecciono a la url emitirInfraccion despues de aver ingresado los datos
		return redirect('/emitirInfraccion/')

@csrf_exempt
def crear_notificacion(request):#no estoy llegando aki 
	print "estoy en Django:"
	print request.POST
	'''multa.objects.create(
				hora = request.POST['hora'],
				descripcion = request.POST['descripcion'],
				Codigo = request.POST['Codigo'],
				fecha_presentacion=request.POST['fecha_presentacion']
		)'''
	m=multa()
	m.idUser=request.POST['idUser']
	m.Usuario=request.POST['Usuario']
	m.descripcion=request.POST['descripcion']
	m.Codigo=request.POST['Codigo']
	m.fecha_presentacion=request.POST['fecha_presentacion']
	m.hora=request.POST['hora']
	m.save()
	cont=multa.objects.all().count()
	print 'cuante las multas',cont
	response = JsonResponse({'cont':cont,
							'idUser':request.POST['idUser'],
							'Usuario':request.POST['Usuario'],
							'descripcion':request.POST['descripcion'],
							'Codigo':request.POST['Codigo'],
							'fecha_presentacion':request.POST['fecha_presentacion'],
							'hora': request.POST['hora']})
	#esto informacion mandamos al server 
	#print response
	return HttpResponse(response.content)

class AvisosDenunciasCliente(TemplateView):
	def get(self, request, *args, **kwargs):
		comments=Comment.objects.all().order_by("-id")[0:5]
		user=request.user
		dic = {
			'form': Commentform(),
			'comments':comments,
			'user':user
				#'nego':nego,
				#'idNe':idNe
		}
			#una ves optenido el nombre enviamos al templete cliente.html
		return render(request, 'inspector/denunciasCliente.html', dic)
		
	def post(self, request, *args, **kwargs):
		"""Comment.objects.create(
				user = request.session['name'],
				comment = request.POST['comment'],
				idNegocio = request.POST['idNegocio']
			)"""
		return redirect('/Denuncias-cliente/')

def VerDenunciasInspector(request,id):
	user=User.objects.get(id=int(id))
	notificacion=multa.objects.all()
	return render_to_response('inspector/MisNotificaciones.html',{'notificacion':notificacion,'user':user},context_instance=RequestContext(request))
def EditarNotificacion(request,id):
	notificacion=multa.objects.get(id=int(id))
	if request.method=='POST':
		form=FormMultaEditar(request.POST,instance=notificacion)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('/')
	else:
		form=FormMultaEditar(instance=notificacion)
	return render_to_response('inspector/EditarNotoficacion.html',{'form':form},context_instance=RequestContext(request))

def datosDenuncia(request,id):
	nego=Negocio.objects.get(id=int(id))
	datosN=multa.objects.filter(Codigo=int(id)).order_by('-id')[0:20]
	return render_to_response('inspector/datosDenuncia.html',{'datosN':datosN,'nego':nego},context_instance=RequestContext(request))
def detaDenuncias(request,id):
	denuncia=multa.objects.filter(id=int(id))
	nombre=Negocio.objects.all()
	return render_to_response('inspector/DenunciaNegocioDetalle.html',{'denuncia':denuncia,'nombre':nombre},context_instance=RequestContext(request))