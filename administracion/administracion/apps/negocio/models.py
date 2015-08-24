from django.db import models

# Create your models here.
class Categoria(models.Model):
	categoria=models.CharField(max_length=50)
	def __unicode__(self):
		return self.categoria

class Negocio(models.Model):
	propietario = models.CharField(max_length=100)
	memorial_apertura = models.CharField(max_length=20)
	resolucion_municipal = models.CharField(max_length=20)
	#categoria=models.CharField(max_length=50)
	direccion=models.CharField(max_length=80)
	categoria=models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.propietario

class multa(models.Model):
	idUser=models.IntegerField()
	Usuario=models.CharField(max_length=100)
	fecha_notificacion=models.DateTimeField(auto_now=True)
	descripcion=models.TextField()
	#opservaciones=models.CharField(max_length=150)
	Codigo=models.IntegerField()# es el ID del Negocio
	fecha_presentacion=models.DateField()
	hora=models.CharField(max_length=12)
	def __unicode__(self):
		return self.Usuario

#class Multa_Pago(models.Model):




