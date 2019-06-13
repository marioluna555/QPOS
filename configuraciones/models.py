from django.db import models

# Create your models here.

class bot_lin_pais(models.Model):
    za_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=25, null=False)
    abreviatura = models.CharField(max_length=12, null=False)
    codigo_telefonico = models.CharField(max_length=10, null=False)
    activo = models.BooleanField(null=False)

class bot_lin_departamento(models.Model):
    za_departamento = models.IntegerField(primary_key=True)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )

    nombre_departamento = models.CharField(max_length=35, null=False)
    abreviatura = models.CharField(max_length=12, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_departamento", "za_pais"))

class bot_lin_municipio(models.Model):
    za_municipio = models.IntegerField(primary_key=True, null=False)
    za_departamento = models.ForeignKey(
        'bot_lin_departamento',
        on_delete = models.CASCADE,
        name='za_departamento'
    )

    za_pais = models.ForeignKey(
        'bot_lin_departamento',
        on_delete = models.CASCADE,
        name='za_pais'
    )

    nombre_municipio = models.CharField(max_length=35, null=False)
    abreviatura = models.CharField(max_length=12, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_municipio", "za_departamento", "za_pais"))

class bot_lin_unidad_medida(models.Model):
    za_unidad_medida = models.IntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

class bot_lin_tipo_documento(models.Model):
    za_tipo_documento = models.IntegerField(primary_key=True, null=False)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )

    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.BooleanField()

class bot_lin_tipo_establecimiento(models.Model):
    za_tipo_establecimiento = models.IntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

class bot_lin_tipo_regimen_fiscal(models.Model):
    za_regimen_fiscal = models.IntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

class bot_lin_tipo_dato(models.Model):
    za_tipo_dato = models.IntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

class bot_lin_tipo_tabla(models.Model):
    za_tipo_tabla = models.IntegerField(primary_key=True, null=False)
    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_dato',
        on_delete = models.CASCADE
    )

    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_tipo_tabla", "za_tipo_dato"))

class bot_modulos(models.Model):
    za_modulo = models.IntegerField(primary_key=True, null=False)
    nombre_modulo = models.CharField(max_length=50, null=False)
    ico_modulo = models.CharField(max_length=12, null=False)
    activo = models.BooleanField(null=False)

class bot_opciones_modulo(models.Model):
    za_opcion_modulo = models.IntegerField(primary_key=True, null=False)
    za_modulo = models.ForeignKey(
        'bot_modulos',
        on_delete=models.CASCADE,
    )
    nombre_opcion = models.CharField(max_length=50, null=False)
    url_opcion = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        unique_together = (("za_opcion_modulo", "za_modulo"))

class bot_empresa(models.Model):
    za_empresa = models.IntegerField(primary_key=True, null=False)
    cod_empresa = models.CharField(max_length=15, null=False)
    razon_social = models.CharField(max_length=200, null=False)
    za_regimen_fiscal = models.IntegerField()
    za_tipo_establecimiento = models.IntegerField()
    direccion_fiscal = models.CharField(max_length=200, null=False)
    telefono1 = models.CharField(max_length=25, null=False)
    telefono2 = models.CharField(max_length=25,null=False)
    email = models.EmailField(max_length=100, null=False)
    fecha_creacion = models.DateTimeField(auto_now=True, null=False)
    activo = models.BooleanField(null=False)


class bot_sucursales_empresa(models.Model):
    za_sucursal = models.IntegerField(primary_key=True, null=False)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    nombre_comercial = models.CharField(max_length=200)
    za_pais = models.ForeignKey(
        'bot_lin_pais',
        on_delete = models.CASCADE
    )
    
    za_depto = models.IntegerField(null=False)

    za_muni = models.IntegerField(null=False)

    zona = models.IntegerField()
    direccion1 = models.CharField(max_length=300)
    direccion2 = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=3000)
    fecha_creacion = models.DateTimeField(auto_now=True, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_sucursal", "za_empresa"))

class bot_lin_estado_empleado(models.Model):
    za_estado = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    descripcion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=15, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_estado", "za_empresa"))

class bot_empleados(models.Model):
    za_empleado = models.IntegerField(primary_key=True, null=False)
    za_empresa = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE,
        name="za_empresa"
    )
    
    za_sucursal = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE,
        name="za_sucursal"
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
        on_delete = models.CASCADE,
        name="za_tipo_documento"
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

    class Meta:
        unique_together = (("za_empleado", "za_empresa", "za_sucursal"))

class bot_repres_legales(models.Model):
    za_repre = models.IntegerField(primary_key=True, null=False)
    za_empresa = models.ForeignKey(
        'bot_empresa',
        on_delete = models.CASCADE
    )

    observaciones = models.CharField(max_length=3000, null=False)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_despido = models.DateTimeField(null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_repre", "za_empresa"))

class bot_telefono(models.Model):
    za_telefono = models.IntegerField(primary_key=True, null=False)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name='za_tipo_tabla'
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name='za_tipo_dato'
    )

    telefono = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_telefono", "za_tipo_tabla", "za_tipo_dato"))

class bot_email(models.Model):
    za_email = models.IntegerField(primary_key=True, null=False)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_tabla"
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_dato"
    )

    email = models.EmailField(max_length=100, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_email", "za_tipo_tabla", "za_tipo_dato"))

class bot_redes_social(models.Model):
    za_red_social = models.IntegerField(primary_key=True, null=False)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_tabla"
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_dato"
    )

    url = models.CharField(max_length=900, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_red_social", "za_tipo_tabla", "za_tipo_dato"))

class bot_sitios(models.Model):
    za_sitio = models.IntegerField(primary_key=True, unique=True)
    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_tabla"
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_dato"
    )

    url = models.CharField(max_length=200, null=False)
    activo = models.BooleanField(null=False)

    class Meta:
        unique_together = (("za_sitio", "za_tipo_tabla", "za_tipo_dato"))

class bot_documentos(models.Model):
    za_doc = models.IntegerField(primary_key=True, unique=True)
    za_empresa = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE,
        name="za_empresa"
    )

    za_sucursal = models.ForeignKey(
        'bot_sucursales_empresa',
        on_delete = models.CASCADE,
        name="za_sucursal"
    )

    za_tipo_tabla = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_tabla"
    )

    za_tipo_dato = models.ForeignKey(
        'bot_lin_tipo_tabla',
        on_delete = models.CASCADE,
        name="za_tipo_dato"
    )

    url_doc = models.CharField(max_length=900, null=False)
    activo = models.BooleanField(null=False)