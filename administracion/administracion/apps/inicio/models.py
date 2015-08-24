from django.db import models
from django.contrib.auth.forms import User
# Create your models here.
class Cronograma(models.Model):
	Usuario = models.ForeignKey(User)
	Fecha_inicio = models.DateField()
	Conclucion = models.DateField()
	Detalle = models.TextField()
	fecha_publicacion=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.Detalle