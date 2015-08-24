from django.db import models
#from administracion.apps.negocio.models import Negocio
# Create your models here.
class Comment(models.Model):
	user = models.CharField(max_length=50)
	comment = models.TextField()
	idNegocio=models.IntegerField()
	fecha_denuncia=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.user