drop database if exists qpos;

create database qpos default character set utf8 collate utf8_spanish_ci;

use qpos;

drop table if exists bot_lin_paises;

create table bot_lin_paises(
	za_pais smallint not null,
    nombre_pais varchar(25) not null,
    abreviatura varchar(12) not null,
    codigo_telefonico varchar(10) not null,
    activo tinyint not null,
    constraint PK_paises primary key(za_pais)
);

drop table if exists bot_lin_departamentos;

create table bot_lin_departamentos(
	za_departamento smallint not null,
    za_pais smallint not null,
    nombre_departamento varchar(35) not null,
    abreviatura varchar(12) not null,
    activo tinyint not null,
    constraint PK_deptos primary key(za_pais,za_departamento),
    constraint FK_lin_deptos_lin_paises foreign key(za_pais)
				references bot_lin_paises(za_pais),
	unique(za_pais,za_departamento)
);

drop table if exists bot_lin_municipios;

create table bot_lin_municipios(
	za_municipio smallint not null,
    za_departamento smallint not null,
    za_pais smallint not null,
    nombre_municipio varchar(35) not null default '',
    abreviatura varchar(12) not null default '',
    activo tinyint,
    constraint PK_munis primary key(za_pais,za_departamento,za_municipio),
    constraint FK_lin_munis_lin_deptos foreign key(za_pais,za_departamento)
				references bot_lin_departamentos(za_pais,za_departamento),
	unique(za_pais,za_departamento,za_municipio)
);

drop table if exists bot_lin_unidad_medida;

create table bot_lin_unidad_medida(
	za_unidad_medida smallint not null,
    descripcion varchar(50) not null default '',
    abreviatura varchar(15) not null default '',
    activo tinyint,
    constraint PK_unidadMedida primary key(za_unidad_medida)
);

drop table if exists bot_lin_tipo_documento;

create table bot_lin_tipo_documento(
	za_tipo_documento tinyint not null,
    za_pais smallint not null default 0,
    descripcion varchar(50) not null,
    abreviatura varchar(15) not null default '',
    activo tinyint not null,
    constraint PK_tipo_documento primary key(za_pais,za_tipo_documento),
    constraint FK_lin_tipo_doc_lin_pais foreign key(za_pais)
				references bot_lin_paises(za_pais),
	unique(za_pais,za_tipo_documento)
);

drop table if exists bot_lin_tipo_establecimiento;

create table bot_lin_tipo_establecimiento(
	za_tipo_establecimiento tinyint not null,
    descripcion varchar(50) not null,
    abreviatura varchar(15) not null default '',
    activo tinyint,
    constraint PK_tipo_establecimiento primary key(za_tipo_establecimiento)
);

drop table if exists bot_lin_tipo_regimen_fiscal;

create table bot_lin_tipo_regimen_fiscal(
	za_regimen_fiscal tinyint not null,
    descripcion varchar(50) not null,
    abrevitura varchar(15) not null default '',
    activo tinyint,
    constraint PK_tipo_regimon_fiscal primary key(za_regimen_fiscal)
);

drop table if exists bot_lin_tipo_datos;

create table bot_lin_tipo_datos(
	za_tipo_dato smallint not null,
    descripcion varchar(50) not null,
    abreviatura varchar(15) not null default '',
    activo tinyint,
    constraint PK_tipo_datos primary key(za_tipo_dato)
);

drop table if exists bot_lin_tipo_tabla;

create table bot_lin_tipo_tabla(
	za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    descripcion varchar(50) not null,
    abrevitura varchar(15) not null,
    activo tinyint not null default 1,
    constraint PK_tipo_tabla primary key(za_tipo_dato,za_tipo_tabla),
    constraint FK_lin_tipo_tabla_lin_tipo_datos foreign key(za_tipo_dato)
				references bot_lin_tipo_datos(za_tipo_dato),
	unique(za_tipo_dato,za_tipo_tabla)
);

drop table if exists bot_empresas;

create table bot_empresas(
	za_empresa smallint not null,
    cod_empresa varchar(15) not null default '',
    razon_social varchar(200) not null default '',
    za_regimen_fiscal tinyint not null,
    za_tipo_establecimiento tinyint not null,
    direccion_fiscal varchar(200) not null default '',
    telefono1 varchar(25) not null default '',
    telefono2 varchar(25) not null default '',
    email varchar(70) not null default '',
    fecha_creacion datetime not null default now(),
    activo tinyint not null default 1,
    constraint PK_empresas primary key(za_empresa)
);

drop table if exists bot_sucursales_empresas;

create table bot_sucursales_empresas(
	za_sucursal smallint not null,
    za_empresa smallint not null,
    nombre_comercial varchar(200) not null,
    za_pais smallint not null,
    za_depto smallint not null,
    za_muni smallint not null,
    zona tinyint not null,
    direccion1 varchar(300) not null default '',
    direccion2 varchar(300) not null default '',
    descripcion varchar(3000) not null default '',
    fecha_creacion datetime not null default now(),
    activo tinyint not null default 1,
    constraint PK_sucursales primary key(za_empresa,za_sucursal),
    constraint FK_sucursales_bot_empresas foreign key(za_empresa)
				references bot_empresas(za_empresa),
	unique(za_empresa,za_sucursal)
);

drop table if exists bot_lin_estado_empleado;

create table bot_lin_estado_empleado(
	za_estado tinyint not null,
    za_empresa smallint not null,
    descripcion varchar(50) not null,
    abreviatura varchar(15) not null default '',
    activo tinyint not null,
    constraint PK_estado_empleado primary key(za_empresa,za_estado),
    constraint FK_lin_estado_emp_bot_empresas foreign key(za_empresa)
				references bot_empresas(za_empresa)
);

drop table if exists bot_empleados;

create table bot_empleados(
	za_empleado smallint not null,
    za_empresa smallint not null,
    za_sucursal smallint not null,
    primer_nom varchar(50) not null,
    segundo_nom varchar(50) not null,
    otros_nombres varchar(100) not null,
    primer_ape varchar(50) not null,
    segundo_ape varchar(50) not null,
    cod_empleado varchar(20) not null default '',
    salario numeric(10,2) not null default 0.00,
    za_tipo_doc smallint not null,
    za_pais smallint not null,
    fecha_inicio datetime not null,
    fecha_despido datetime,
    za_estado tinyint not null,
    constraint PK_empleados primary key(za_empresa,za_sucursal,za_empleado),
    constraint FK_empleados_bot_sucursales foreign key(za_empresa,za_sucursal)
				references bot_sucursales_empresas(za_empresa,za_sucursal),
	unique(za_empresa,za_sucursal,za_empleado)
);

drop table if exists bot_repres_legales;

create table bot_repres_legales(
	za_repre tinyint not null,
    za_empleado smallint not null,
    za_empresa smallint not null,
    za_sucursal smallint not null,
    observaciones varchar(3000) not null default '',
    fecha_inicio datetime not null default now(),
    fecha_despido datetime,
    activo tinyint not null default 1,
    constraint PK_repre_legal primary key(za_empresa,za_sucursal,za_empleado,za_repre),
    constraint FK_repres_bot_empleados foreign key(za_empresa,za_sucursal,za_empleado)
				references bot_empleados(za_empresa,za_sucursal,za_empleado),
	unique(za_empresa,za_sucursal,za_empleado,za_repre)
);

drop table if exists bot_usuarios;

create table bot_usuarios(
	za_usuario smallint not null,
    za_empresa smallint not null,
    za_sucursal smallint not null,
    usuario varchar(25) not null,
    contra varbinary(200),
    nombre_usuario varchar(400) not null default '',
    za_empleado smallint not null default 0,
    codigo_usuario varchar(15) not null default '',
    activo tinyint not null default 1,
    constraint PK_usuarios primary key(za_empresa,za_sucursal,za_usuario),
    constraint FK_usuarios_bot_sucursales foreign key(za_empresa,za_sucursal)
				references bot_empresas(za_empresa,za_sucursal),
	unique(za_empresa,za_sucursal,za_usuario)
);