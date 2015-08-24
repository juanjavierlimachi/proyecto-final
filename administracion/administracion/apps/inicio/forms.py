#encoding:utf-8
from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *
from django.forms.extras.widgets import SelectDateWidget

class FormCronograma(forms.ModelForm):
	Fecha_inicio = forms.DateField(widget=SelectDateWidget())
	Conclucion = forms.DateField(widget=SelectDateWidget())
	class Meta:
		model=Cronograma
		exclude=('Usuario',)
