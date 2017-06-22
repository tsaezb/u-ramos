from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ramo(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Profe(models.Model):
    name = models.CharField(max_length=50)
    ramos = models.ManyToManyField(Ramo)

    def __str__(self):
        return self.name
        
class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    profe = models.ForeignKey(Profe)
    ramo = models.ForeignKey(Ramo)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

class Sugerencia(models.Model):
    texto = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)