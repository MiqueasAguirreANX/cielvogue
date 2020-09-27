from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=45)
    talle = models.CharField(max_length=6, choices=[('Small','Small'), ('Large', 'Large')], default='S')
    precioSmall = models.FloatField()
    precioLarge = models.FloatField()
    scriptMPL = models.TextField(default="<div class='btn btn-danger'>Error</div>")
    scriptMPS = models.TextField(default="<div class='btn btn-danger'>Error</div>")
    imagen = models.ImageField(upload_to='static/imagenes')

    def __str__(self):
        return self.nombre

    def patronS(self):
        return "imagenes/"+self.nombre+".jpeg"