from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Autor
from .models import Entrada
from .forms import *
"""def welcome(request):
	return HttpResponse('<center><h1>Welcome to this Site</h1></center>')"""
def welcome(request):
	return render(request,'welcome.html')
def autores(request):
	if request.method == 'POST':
		form = AutorForm(request.POST)
		if form.is_valid():
			autor = Autor()
			autor.nombres = form.cleaned_data['nombres']
			autor.apellidos = form.cleaned_data['apellidos']
			autor.save()
			return redirect('autores')
	else:
		form=AutorForm
		todosAutores=Autor.objects.all()
		return render(request,'autores.html',{'autores':todosAutores,'form':form})
def edit_autor(request, id):
	autor = Autor.objects.get(id_autor=id)
	form= AutorForm(instance=autor)
	if request.method=='POST':
		form_cambiado=AutorForm(request.POST, instance=autor)
		if form_cambiado.is_valid():
			form_cambiado.save()
			return redirect('autores')
	else:
		return render(request,'edit_autor.html',{'form':form,'autor':autor})
def delete_autor(request,id):
	autor = Autor.objects.get(id_autor=id)
	autor.delete()
	return redirect('autores')
def entradas(request):
	form2=EntradaForm
	todasEntradas=Entrada.objects.all()
	return render(request,'entradas.html',{'entradas':todasEntradas,'form2':form2})
	"""form2 = EntradaForm
    return render(request, 'entradas.html', {'form':form2})"""


