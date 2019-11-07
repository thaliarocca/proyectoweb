from django import forms
from .models import *
class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		exclude =['id_autor']
class EntradaForm(forms.ModelForm):
	class Meta:
		model = Entrada
		exclude =['id_ent','fecha_hora']