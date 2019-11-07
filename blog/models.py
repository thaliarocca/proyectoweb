from django.db import models

# Create your models here.
class Entrada(models.Model):
	id_ent = models.AutoField(primary_key = True)
	titular = models.CharField(max_length = 120)
	fecha_hora = models.CharField(max_length = 120)
	contenido = models.TextField()
	autor = models.ForeignKey('Autor',on_delete=models.CASCADE)
class Autor(models.Model):
	id_autor =  models.AutoField(primary_key = True)
	nombres = models.CharField(max_length = 120)
	apellidos = models.CharField(max_length = 120)
	def __str__(self):
		return self.nombres+' '+self.apellidos