from django.db import models
from django.urls import reverse

class Genero(models.Model):  
    name = models.CharField(max_length=64, help_text='Tipo de genero')

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    titulo = models.CharField(max_length=64)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=256, help_text='Descripcion de la pelicula')    
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pelicula-detalle', args=[str(self.id)])

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    fecha_de_defuncion = models.DateField('Difunto', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detalle', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)      