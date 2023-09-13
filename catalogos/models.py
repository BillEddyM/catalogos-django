from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
        nombre = models.CharField(max_length=100)
        codigo = models.CharField(max_length=5)

        def __str__(self):
            return self.nombre
