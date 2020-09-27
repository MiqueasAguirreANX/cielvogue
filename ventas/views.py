from django.shortcuts import render
from ventas.models import Producto

# Create your views here.

def productos(response):
    contexto = {}
    print("\n\n", response.POST ,"\n\n")
    if response.method == "POST":
        return render(response, 'ventas/f_producto.html', contexto)
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