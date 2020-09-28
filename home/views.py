from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.messages import error, success
# Create your views here.

def inicio(request):
    contexto = {}
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                success(request, "Bienvenid@ de vuelta "+str(user)+"!")
            else:
                error(request, "Usted todavia no es un usuario! Registrese porfavor")
        else:
            error(request, "Datos no validos")

    return render(request, 'home/inicio.html', contexto)

def contacto(response):
    contexto = {}
    return render(response, 'home/contacto.html', contexto)