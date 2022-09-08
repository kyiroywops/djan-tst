from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def libros(request):
    return render(request, "libros/index.html")
def crear(request):
    return render(request, "libros/crear.html")