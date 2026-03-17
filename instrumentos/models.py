from django.db import models

class Instrumento(models.Model):
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self): 
        return f"Instrumento:{self.nombre} - ({self.tipo})" 
    
class Marca(models.Model):
    
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=20)

    def __str__(self):
        return f"Marca:{self.nombre} - ({self.pais})"
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    dni = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"Cliente:{self.nombre}-{self.apellido}-{self.email}"

