from django.db import models

# Create your models here.

class bot_lin_pais(models.Model):
    za_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=25)
    abreviatura = models.CharField(max_length=12)
    codigo_telefonico = models.CharField(max_length=10)
    activo = models.BooleanField()

class bot_lin_departamento(models.Model):
    za_departamento = models.IntegerField(primary_key=True, unique=True)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete=models.CASCADE,
    )

    nombre_departamento = models.CharField(max_length=35)
    abreviatura = models.CharField(max_length=12)
    activo = models.BooleanField()