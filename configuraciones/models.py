# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BotEmpleados(models.Model):
    za_empleado = models.SmallIntegerField()
    za_empresa = models.ForeignKey('BotSucursalesEmpresas', models.DO_NOTHING, db_column='za_empresa', primary_key=True)
    za_sucursal = models.ForeignKey('BotSucursalesEmpresas', models.DO_NOTHING, db_column='za_sucursal')
    primer_nom = models.CharField(max_length=50)
    segundo_nom = models.CharField(max_length=50)
    otros_nombres = models.CharField(max_length=100)
    primer_ape = models.CharField(max_length=50)
    segundo_ape = models.CharField(max_length=50)
    cod_empleado = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    za_tipo_doc = models.SmallIntegerField()
    za_pais = models.SmallIntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_despido = models.DateTimeField(blank=True, null=True)
    za_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_empleados'
        unique_together = (('za_empresa', 'za_sucursal', 'za_empleado'), ('za_empresa', 'za_sucursal', 'za_empleado'),)


class BotEmpresas(models.Model):
    za_empresa = models.SmallIntegerField(primary_key=True)
    cod_empresa = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=200)
    za_regimen_fiscal = models.IntegerField()
    za_tipo_establecimiento = models.IntegerField()
    direccion_fiscal = models.CharField(max_length=200)
    telefono1 = models.CharField(max_length=25)
    telefono2 = models.CharField(max_length=25)
    email = models.CharField(max_length=70)
    fecha_creacion = models.DateTimeField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_empresas'


class BotLinDepartamentos(models.Model):
    za_departamento = models.SmallIntegerField()
    za_pais = models.ForeignKey('BotLinPaises', models.DO_NOTHING, db_column='za_pais', primary_key=True)
    nombre_departamento = models.CharField(max_length=35)
    abreviatura = models.CharField(max_length=12)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_lin_departamentos'
        unique_together = (('za_pais', 'za_departamento'), ('za_pais', 'za_departamento'),)


class BotLinEstadoEmpleado(models.Model):
    za_estado = models.IntegerField()
    za_empresa = models.ForeignKey(BotEmpresas, models.DO_NOTHING, db_column='za_empresa', primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_lin_estado_empleado'
        unique_together = (('za_empresa', 'za_estado'),)


class BotLinMunicipios(models.Model):
    za_municipio = models.SmallIntegerField()
    za_departamento = models.ForeignKey(BotLinDepartamentos, models.DO_NOTHING, db_column='za_departamento')
    za_pais = models.ForeignKey(BotLinDepartamentos, models.DO_NOTHING, db_column='za_pais', primary_key=True)
    nombre_municipio = models.CharField(max_length=35)
    abreviatura = models.CharField(max_length=12)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_lin_municipios'
        unique_together = (('za_pais', 'za_departamento', 'za_municipio'), ('za_pais', 'za_departamento', 'za_municipio'),)


class BotLinPaises(models.Model):
    za_pais = models.SmallIntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=25)
    abreviatura = models.CharField(max_length=12)
    codigo_telefonico = models.CharField(max_length=10)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_lin_paises'


class BotLinTipoDatos(models.Model):
    za_tipo_dato = models.SmallIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_lin_tipo_datos'


class BotLinTipoDocumento(models.Model):
    za_tipo_documento = models.IntegerField()
    za_pais = models.ForeignKey(BotLinPaises, models.DO_NOTHING, db_column='za_pais', primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_lin_tipo_documento'
        unique_together = (('za_pais', 'za_tipo_documento'), ('za_pais', 'za_tipo_documento'),)


class BotLinTipoEstablecimiento(models.Model):
    za_tipo_establecimiento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_lin_tipo_establecimiento'


class BotLinTipoRegimenFiscal(models.Model):
    za_regimen_fiscal = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    abrevitura = models.CharField(max_length=15)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_lin_tipo_regimen_fiscal'


class BotLinTipoTabla(models.Model):
    za_tipo_tabla = models.SmallIntegerField()
    za_tipo_dato = models.ForeignKey(BotLinTipoDatos, models.DO_NOTHING, db_column='za_tipo_dato', primary_key=True)
    descripcion = models.CharField(max_length=50)
    abrevitura = models.CharField(max_length=15)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_lin_tipo_tabla'
        unique_together = (('za_tipo_dato', 'za_tipo_tabla'), ('za_tipo_dato', 'za_tipo_tabla'),)


class BotLinUnidadMedida(models.Model):
    za_unidad_medida = models.SmallIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=15)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_lin_unidad_medida'


class BotRepresLegales(models.Model):
    za_repre = models.IntegerField()
    za_empleado = models.ForeignKey(BotEmpleados, models.DO_NOTHING, db_column='za_empleado')
    za_empresa = models.ForeignKey(BotEmpleados, models.DO_NOTHING, db_column='za_empresa', primary_key=True)
    za_sucursal = models.ForeignKey(BotEmpleados, models.DO_NOTHING, db_column='za_sucursal')
    observaciones = models.CharField(max_length=3000)
    fecha_inicio = models.DateTimeField()
    fecha_despido = models.DateTimeField(blank=True, null=True)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_repres_legales'
        unique_together = (('za_empresa', 'za_sucursal', 'za_empleado', 'za_repre'), ('za_empresa', 'za_sucursal', 'za_empleado', 'za_repre'),)


class BotSucursalesEmpresas(models.Model):
    za_sucursal = models.SmallIntegerField()
    za_empresa = models.ForeignKey(BotEmpresas, models.DO_NOTHING, db_column='za_empresa', primary_key=True)
    nombre_comercial = models.CharField(max_length=200)
    za_pais = models.SmallIntegerField()
    za_depto = models.SmallIntegerField()
    za_muni = models.SmallIntegerField()
    zona = models.IntegerField()
    direccion1 = models.CharField(max_length=300)
    direccion2 = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=3000)
    fecha_creacion = models.DateTimeField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_sucursales_empresas'
        unique_together = (('za_empresa', 'za_sucursal'), ('za_empresa', 'za_sucursal'),)


class BotUsuarios(models.Model):
    za_usuario = models.SmallIntegerField()
    za_empresa = models.SmallIntegerField(primary_key=True)
    za_sucursal = models.SmallIntegerField()
    usuario = models.CharField(max_length=25)
    contra = models.CharField(max_length=200, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=400)
    za_empleado = models.SmallIntegerField()
    codigo_usuario = models.CharField(max_length=15)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bot_usuarios'
        unique_together = (('za_empresa', 'za_sucursal', 'za_usuario'), ('za_empresa', 'za_sucursal', 'za_usuario'),)
