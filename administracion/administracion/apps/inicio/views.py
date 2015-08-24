from django.shortcuts import render, render_to_response,redirect
from django.views.generic import TemplateView, FormView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from administracion.apps.cliente.models import Comment
from administracion.apps.cliente.forms import Commentform
from .forms import *
from administracion.apps.negocio.models import multa
from administracion.apps.inspector.forms import *
from django.core import serializers

# Create your views here.
class AvisosDenuncias(TemplateView):
	def get(self, request, *args, **kwargs):
		#idNe=request.GET.get('id')#puede ser una opcion para enviar el id del negocio
		#nego=Negocio.objects.get(id=idNe)
		#print "este es el negocio:",nego
		#if request.session.get('name'):
		cuantaDenuncias=Comment.objects.all().count()
		comments=Comment.objects.all().order_by("-id")[0:5]
			#este es el formato de la url en el QR http://localhost:8000/denuncias/?id=23
		dic = {
				#'ne':request.GET.get('id'),#asi mento el num envio en id del negocio mediante
			'cont':cuantaDenuncias,
			'form': Commentform(),
			'comments':comments
		}
			#una ves optenido el nombre enviamos al templete cliente.html
		return render(request, 'inicio/denuncias.html', dic)
		
	def post(self, request, *args, **kwargs):
		"""Comment.objects.create(
				user = request.session['name'],
				comment = request.POST['comment'],
				idNegocio = request.POST['idNegocio']
			)"""
		return redirect('/AvisosDenuncias/')

class AvisosNotificaciones(TemplateView):
	def get(self, request, *args, **kwargs):
		multas=multa.objects.all().order_by("-id")[0:4]
		contexto=request.user
		contarmultas = multa.objects.all().count()
		dic = {
			'cont':contarmultas,
			'user':contexto,
			'form': FormMulta(),
			'multa':multas
		}
		#una ves optenido el nombre enviamos al templete cliente.html
		return render(request, 'inicio/Notificaciones.html', dic)
	def post(self, request, *args, **kwargs):
		print 'as guardado la informacion'
		multa.objects.create(
				idUser = request.POST['idUser'],
				Usuario = request.POST['Usuario'],
				descripcion = request.POST['descripcion'],
				Codigo = request.POST['Codigo'],
				fecha_presentacion=request.POST['fecha_presentacion'],
				hora = request.POST['hora']
			)
		return redirect('/privado/')
def EnviarNotificacion(request):

	return render_to_response('inicio/formAvisos.html',{},context_instance=RequestContext(request))

def Notiicaciones(request,id):
	return render_to_response('inicio/NotificacionesNegocio.html',{},context_instance=RequestContext(request))

def RegistroCronograma(request):
	if request.method == 'POST':
		Usuario=Cronograma(Usuario=request.user)
		form=FormCronograma(request.POST,instance=Usuario)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Cronograma/')
	else:
		form=FormCronograma()
	return render_to_response('inicio/registroConograma.html',{'form':form},context_instance=RequestContext(request))
def datosDenuncia(request,id):
	nego=Negocio.objects.get(id=int(id))
	datosN=multa.objects.filter(Codigo=int(id)).order_by('-id')[0:20]
	return render_to_response('inicio/DatosNegocio.html',{'datosN':datosN,'nego':nego},context_instance=RequestContext(request))
def detDenuncias(request,id):
	denuncia=multa.objects.filter(id=int(id))
	nombre=Negocio.objects.all()
	return render_to_response('inicio/DenunciaNegocio.html',{'denuncia':denuncia,'nombre':nombre},context_instance=RequestContext(request))

def DetalleDenuncias(request, id):
	nego=Negocio.objects.all()
	denuncia=Comment.objects.filter(id=int(id))
	return render_to_response('inicio/DatosDenunciaCliente.html',{'denuncia':denuncia,'nego':nego},context_instance=RequestContext(request))

def VerNotificacionesInspector(request,id):
	inspecciones=multa.objects.filter(idUser=int(id)).order_by('-id')[0:20]
	print inspecciones
	nego=Negocio.objects.all()
	return render_to_response('inicio/MisInspecciones.html',{'inspecciones':inspecciones,'nego':nego},context_instance=RequestContext(request))

def TodaslasNotificaciones(request):
	ns=multa.objects.all().order_by('-id')[0:200]
	return render_to_response('inicio/TodaslasNotificaciones.html',{'ns':ns},context_instance=RequestContext(request))
def TodaslasDenuncias(request):
	cs=Comment.objects.all().order_by('-id')[0:200]
	print 'estas son las notificacions'
	print cs
	return render_to_response('inicio/TodaslasComentarios.html',{'cs':cs},context_instance=RequestContext(request))

class ConsultarDenunciaFecha(TemplateView):
	def get(self, request, *args, **kwargs):
		fechas = request.GET['fe']
		fin=request.GET['fn']
		
		print fechas
		print fin
		#fecha = fecha.strftime("%Y/%m/%d")ponemos un formato a la fecha __gte es >=
		#consulta = multa.objects.filter(fecha_notificacion__gte=fechas,fecha_notificacion__Ite=fin)
		consulta = multa.objects.filter(fecha_notificacion__range=(fechas,fin))
		print 'Esta es la fecha:',consulta
		data = serializers.serialize('json', consulta,fields=('id','Usuario','fecha_notificacion','descripcion'))
		return HttpResponse(data, 'application/json')

class ConsultarDenunciaClienteFecha(TemplateView):
	def get(self, request, *args, **kwargs):
		fechas = request.GET['fe']
		fin=request.GET['fn']
		
		print fechas
		print fin
		#fecha = fecha.strftime("%Y/%m/%d")ponemos un formato a la fecha __gte es >=
		#consulta = multa.objects.filter(fecha_notificacion__gte=fechas,fecha_notificacion__Ite=fin)
		consulta = Comment.objects.filter(fecha_denuncia__range=(fechas,fin))
		print 'Esta es la fecha:',consulta
		data = serializers.serialize('json', consulta,fields=('id','user','fecha_denuncia','comment'))
		return HttpResponse(data, 'application/json')