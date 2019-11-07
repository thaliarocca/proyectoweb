from django.contrib import admin

from .models import Entrada
from .models import Autor

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
	pass
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	pass
