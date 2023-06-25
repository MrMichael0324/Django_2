from django.db import models

class ModInscripción(models.Model):
    Nombre = models.CharField(max_length=100)
    NumeroTelefono = models.IntegerField()
    FechaSeminario = models.DateField()
    Empresa_Institucion = models.CharField(max_length=100)
    Email = models.EmailField()
    Profesion = models.CharField(max_length=100)
    Observaciones = models.TextField()

    
