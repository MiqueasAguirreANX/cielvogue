from django.shortcuts import render

# Create your views here.

def inicio(response):
    contexto = {}
    return render(response, 'home/inicio.html', contexto)

def contacto(response):
    contexto = {}
    return render(response, 'home/contacto.html', contexto)