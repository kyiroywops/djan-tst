from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>hola mundo</h1>")

# Create your views here.
