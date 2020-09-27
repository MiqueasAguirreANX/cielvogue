from django.shortcuts import render, redirect
from ventas.models import Producto
from django.contrib.messages import error

# Create your views here.

def productos(response):
    contexto = {}
    if response.method == "POST":
        try:
            nombre = response.POST.get("nombre")  
            producto = Producto.objects.get(nombre=nombre)
            contexto["producto"]= producto
            print("\nprimer post")
            print(response.POST ,"\n\n")
            return render(response, 'ventas/f_producto.html', contexto)
        except :
            try:
                print("\nsegundo post")
                print(response.POST ,"\n\n")
                contexto = {}
                largo = response.POST.get("radios")
                contexto["largo"] = largo
                nombre = response.POST.get("titulo")
                producto = Producto.objects.get(nombre=nombre)
                contexto["producto"]= producto
                return render(response, 'ventas/seguro.html', contexto)
            except :
                return redirect('/')
    else:
        if Producto.objects.all():
            lista = []
            for prd in Producto.objects.all():
                lista.append("imagenes/"+str(prd.nombre)+".jpeg")
            contexto["productos"] = Producto.objects.all()
            contexto["nombres"] = lista
        return render(response, 'ventas/productos.html', contexto)

def detalles(response):
    contexto = {}
    return render(response, 'ventas/f_producto.html', contexto)