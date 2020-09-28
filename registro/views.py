from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.messages import error, success

# Create your views here.

def registro(request):
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                success(request, "Bienvenid@ "+str(user)+"! te has registrado correctamente")
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
            else:
                error(request, "Hubo un fallo al crear el usuario! Intente de vuelta")
                return redirect('/')
        else:
            error(request, "Datos no validos")
            return redirect('/')

    else:
        form = UserCreationForm()
    return render(request, "registro/registro.html", {"form":form})

def inicio_sesion(request):
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
                success(request, "Bienvenid@ de vuelta "+str(user)+"!")
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
            else:
                error(request, "Usted todavia no es un usuario! Registrese porfavor")
                return redirect('/')
        else:
            error(request, "Datos no validos")
            return redirect('/')

    # Si llegamos al final renderizamos el formulario
    else:
        form = AuthenticationForm()
        return render(request, "registro/inicio_sesion.html", {'form': form})

def cerrar_sesion(response):
    logout(response)
    return redirect("/")