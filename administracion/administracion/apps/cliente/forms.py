from django import forms
from .models import *
class Commentform(forms.ModelForm):
	class Meta:
		model=Comment