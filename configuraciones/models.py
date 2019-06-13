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

class bot_lin_municipio(models.Model):
    za_municipio = models.IntegerField(primary_key=True, unique=True)
    za_departamento = models.ForeignKey(
        'bot_lin_departamento',
        on_delete = models.CASCADE
    )

    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )

    nombre_municipio = models.CharField(max_length=35)
    abreviatura = models.CharField(max_length=12)
    activo = models.BooleanField()

class bot_lin_unidad_medida(models.Model):
    za_unidad_medida = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_lin_tipo_establecimiento(models.Model):
    za_tipo_establecimiento = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_lin_tipo_regimen_fiscal(models.Model):
    za_regimen_fiscal = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_lin_tipo_dato(models.Model):
    za_tipo_dato = models.IntegerField(primary_key=True, unique=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_lin_tipo_tabla(models.Model):
    za_tipo_tabla = models.IntegerField(primary_key=True, unique=True)
    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_dato',
        on_delete = models.CASCADE
    )

    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_modulos(models.Model):
    za_modulo = models.IntegerField(primary_key=True, unique=True)
    nombre_modulo = models.CharField(max_length=50)
    ico_modulo = models.CharField(max_length=12)
    activo = models.BooleanField()

class bot_opciones_modulo(models.Model):
    za_opcion_modulo = models.IntegerField(primary_key=True, unique=True)
    za_modulo = models.ForeignKey(
        'bot_modulos',
        on_delete=models.CASCADE,
    )
    nombre_opcion = models.CharField(max_length=50)
    url_opcion = models.CharField(max_length=100)
    activo = models.BooleanField()

class bot_empresa(models.Model):
    za_empresa = models.CharField(primary_key=True, unique=True)
    cod_empresa = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=200)
    za_regimen_fiscal = models.IntegerField()
    za_tipo_establecimiento = models.IntegerField()
    direccion_fiscal = models.CharField(max_length=200)
    telefono1 = models.CharField(max_length=25)
    telefono2 = models.CharField(max_lenght=25)
    email = models.EmailField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now=True)
