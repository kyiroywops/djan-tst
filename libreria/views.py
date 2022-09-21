from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {"libros": libros})

def crear(request):
    return render(request, "libros/crear.html")

def editar(request):
    return render(request, "libros/editar.html")

