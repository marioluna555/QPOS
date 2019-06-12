from django.db import models

# Create your models here.

class bot_lin_pais(models.model):
    za_pais = models.intField(max_lenght=4, primary_key=true)
    nombre_pais = models.charField(max_lenght=25)
    abreviatura = models.charField(max_lenght=12)
    codigo_telefonico = models.charField(max_lenght=10)
    activo = models.booleanField()

class bot_lin_departamento(models.model):
    za_departamento = models.intField(max_lenght=5, primary_key=true, unique=true)
    za_pais = models.intField(max_lenght=4, foreign_key=true, unique=true)
    nombre_departamento = models.charField(max_lenght=35)
    abreviatura = models.charField(max_lenght=12)
    activo = models.booleanField()