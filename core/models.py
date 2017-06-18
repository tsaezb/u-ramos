from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ramo(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)
    
class Profe(models.Model):
    name = models.CharField(max_length=50)
    ramos = models.ManyToManyField(Ramo)

