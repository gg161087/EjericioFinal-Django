from django.shortcuts import render
from .models import Genero, Pelicula, Director

def index(request):
    num_peliculas = Pelicula.all().count()
    num_directores = Director.all().count()
    num_generos = Genero.all().count()

    render(
        request,
        'index.html',
        context={
            'num_peliculas' = num_peliculas,
            'num_directores' = num_directores,
            'num_generos' = num_generos
        }
    )