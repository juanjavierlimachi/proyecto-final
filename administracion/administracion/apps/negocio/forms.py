from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget

#TIPO = (('Locales', 'Locales',), ('TIENDAS', 'Tiendas',),('COMERCIOS','Comercios',))
class formNegocio(forms.ModelForm):
	#tipo=forms.ChoiceField(widget=forms.RadioSelect, choices=TIPO)
	class Meta:
		model=Negocio

class buscarForm(forms.Form):
	buscar=forms.CharField()