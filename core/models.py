from __future__ import unicode_literals

import datetime

from django.db import models
from vote.models import VoteModel
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
        
class Comentario(VoteModel,models.Model):
    YEARS = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
    IMPORTANCIA = [(r, r) for r in range(1,8)]
    PRIMAVERA= 'P'
    OTONO = 'O'
    VERANO = 'V'
    SEMESTRES = (
        (PRIMAVERA, 'Primavera'),
        (OTONO, 'Otono'),
        (VERANO, 'Verano'),
    )
    texto = models.CharField(max_length=200)
    profe = models.ForeignKey(Profe)
    ramo = models.ForeignKey(Ramo)
    importancia_asistencia_catedra = models.IntegerField(choices=IMPORTANCIA,default=4)
    importancia_asistencia_auxiliar = models.IntegerField( choices=IMPORTANCIA, default=4)
    exigencia_ramo_profesor = models.IntegerField( choices=IMPORTANCIA, default=4)
    metodos_profesor = models.IntegerField( choices=IMPORTANCIA, default=4)
    recomienda = models.BooleanField(default=False)
    semestre = models.CharField(
        max_length=2,
        choices=SEMESTRES,
        default=PRIMAVERA,
    )
    year = models.IntegerField('year', choices=YEARS, default=datetime.datetime.now().year)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

class Sugerencia(models.Model):
    texto = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)