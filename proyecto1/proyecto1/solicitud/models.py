from django.db import models
from django.contrib.auth.models import User

class Reportes(models.Model):
    problema = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    archivo = models.FileField("Archivo", upload_to='archivo/', max_length=300, default='archivos/terminos.pdf')
    activo = models.BooleanField(default=True)

    
    def __str__(self):
        return str(self.problema)
    

class Personas(models.Model):
    ESTADOS = [ ('1','Chihuahua'),('2','Durango'),('3','Sinaloa') ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(max_length=100, choices=ESTADOS)
    ciudad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)


class cat_Estado(models.Model):

    entidad_federativa = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    default = models.IntegerField(default=0)
    orden = models.IntegerField(default=1)
    codigo = models.CharField(max_length=45, blank=True)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return str(self.entidad_federativa) 