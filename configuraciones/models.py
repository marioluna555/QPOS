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

class bot_lin_tipo_documento(models.Model):
    za_tipo_documento = models.IntegerField(primary_key=True, unique=True)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )

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
    za_empresa = models.IntegerField(primary_key=True, unique=True)
    cod_empresa = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=200)
    za_regimen_fiscal = models.IntegerField()
    za_tipo_establecimiento = models.IntegerField()
    direccion_fiscal = models.CharField(max_length=200)
    telefono1 = models.CharField(max_length=25)
    telefono2 = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField()


class bot_sucursales_empresa(models.Model):
    za_sucursal = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    nombre_comercial = models.CharField(max_length=200)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )
    
    za_depto = models.ForeignKey(
        'bot_lin_departamento',
        on_delete = models.CASCADE
    )

    za_muni = models.ForeignKey(
        'bot_lin_municipio',
        on_delete = models.CASCADE
    )

    zona = models.IntegerField()
    direccion1 = models.CharField(max_length=300)
    direccion2 = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=3000)
    fecha_creacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField()

class bot_lin_estado_empleado(models.Model):
    za_estado = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    za_sucursal = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE
    )

    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_empleados(models.Model):
    za_empleado = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )
    
    za_sucursal = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE
    )

    primer_nom = models.CharField(max_length=50)
    segundo_nom = models.CharField(max_length=50)
    otros_nombres = models.CharField(max_length=100)
    primer_ape = models.CharField(max_length=50)
    segundo_ape = models.CharField(max_length=50)
    cod_empleado = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    za_tipo_doc = models.ForeignKey(
        'bot_lin_tipo_documento',
        on_delete = models.CASCADE
    )

    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )

    fecha_inicio = models.DateTimeField()
    fecha_despido = models.DateTimeField()
    za_estado = models.ForeignKey(
        'bot_lin_estado_empelado',
        on_delete = models.CASCADE
    )

class bot_repres_legales(models.Model):
    za_repre = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    observaciones = models.CharField(max_length=3000)
    fecha_inicio = models.DateTimeField()
    fecha_despido = models.DateTimeField()
    activo = models.BooleanField()

class bot_telefono(models.Model):
    za_telefono = models.IntegerField(primary_key=True, unique=True)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        related_name='bot_lin_tipo_tabla.za_tipo_tabla'
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        related_name='bot_lin_tipo_tabla.za_tipo_dato'
    )

    telefono = models.CharField(max_length=50)
    activo = models.BooleanField()

class bot_email(models.Model):
    za_email = models.IntegerField(primary_key=True, unique=True)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    email = models.EmailField(max_length=100)
    activo = models.BooleanField()

class bot_redes_social(models.Model):
    za_red_social = models.IntegerField(primary_key=True, unique=True)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    url = models.CharField(max_length=900)
    activo = models.BooleanField()

class bot_sitios(models.Model):
    za_sitio = models.IntegerField(primary_key=True, unique=True)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    url = models.CharField(max_length=200)
    activo = models.BooleanField()

class bot_documentos(models.Model):
    za_doc = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_sucursales_empresa.za_empresa',
        on_delete = models.CASCADE
    )

    za_sucursal = models.ForeignKey(
        'bot_sucursales_empresa.za_sucursal',
        on_delete = models.CASCADE
    )

    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE
    )

    url_doc = models.CharField(max_length=900)
    activo = models.BooleanField()


#Los modelos no están terminados porque falta
#Encontrar averiguar porque en las llaves compuestas
#No puedo hacer referencia con llave foranea
#Desde otras tablas