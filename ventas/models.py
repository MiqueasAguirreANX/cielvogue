from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=45)
    talle = models.CharField(max_length=6, choices=[('Small','Small'), ('Large', 'Large')], default='S')
    precioSmall = models.FloatField()
    precioLarge = models.FloatField()
    scriptMP = models.TextField()
    imagen = models.ImageField(upload_to='static/imagenes')

    def __str__(self):
        return self.nombre

    def patronS(self):
        return "imagenes/"+self.nombre+".jpeg"