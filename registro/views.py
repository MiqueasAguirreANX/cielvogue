from django.shortcuts import render, redirect

# Create your views here.

def registro(response):
    contexto = {}
    return render(response, 'registro/registro.html', contexto)

def inicio_sesion(response):
    contexto = {}
    return render(response, 'registro/inicio_sesion.html', contexto)

def cerrar_sesion(response):
    return redirect('/')