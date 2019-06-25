-- El cliente se conectara con usuario de base de datos 'usuario' contra = 'usuario'
-- El usuario del sistema será 'admin' contra = 'admin'

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

drop table if exists bot_telefonos;

create table bot_telefonos(
	za_telefono smallint not null,
    za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    telefono varchar(50) not null,
    activo tinyint not null default 1,
    constraint PK_bot_telefonos primary key(za_tipo_dato,za_tipo_tabla,za_telefono),
    constraint FK_bot_tele_bot_lin_tipo_tabla foreign key(za_tipo_dato,za_tipo_tabla)
				references bot_lin_tipo_tabla(za_tipo_dato,za_tipo_tabla),
	unique(za_tipo_dato,za_tipo_tabla,za_telefono)
);

drop table if exists bot_emails;

create table bot_emails(
	za_email smallint not null,
    za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    email varchar(100) not null,
    activo tinyint not null default 1,
    constraint PK_bot_emails primary key(za_tipo_dato,za_tipo_tabla,za_email),
    constraint FK_bot_emails_bot_lin_tipo_tabla foreign key(za_tipo_dato,za_tipo_tabla)
				references bot_lin_tipo_tabla(za_tipo_dato,za_tipo_tabla),
	unique(za_tipo_dato,za_tipo_tabla,za_email)
);

drop table if exists bot_redes_sociales;

create table bot_redes_sociales(
	za_red_social smallint not null,
    za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    url varchar(900) not null,
    activo tinyint not null default 1,
    constraint PK_bot_redes_sociales primary key(za_tipo_dato,za_tipo_tabla,za_red_social),
    constraint FK_bot_redes_sociales_bot_lin_tipo_tabla foreign key(za_tipo_dato,za_tipo_tabla)
				references bot_lin_tipo_tabla(za_tipo_dato,za_tipo_tabla),
	unique(za_tipo_dato,za_tipo_tabla,za_red_social)
);

drop table if exists bot_sitios;

create table bot_sitios(
	za_sitio smallint not null,
    za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    url varchar(200) not null,
    activo tinyint not null default 1,
    constraint PK_bot_sitios primary key(za_tipo_dato,za_tipo_tabla,za_sitio),
    constraint FK_bot_sitios_bot_lin_tipo_tabla foreign key(za_tipo_dato,za_tipo_tabla)
				references bot_lin_tipo_tabla(za_tipo_dato,za_tipo_tabla),
	unique(za_tipo_dato,za_tipo_tabla,za_sitio)
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
    constraint PK_empresas primary key(za_empresa),
    unique(za_empresa)
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
    fecha_actualizacion datetime not null default now(),
    activo tinyint not null default 1,
    constraint PK_usuarios primary key(za_empresa,za_sucursal,za_usuario),
    -- constraint FK_usuarios_bot_sucursales foreign key(za_empresa,za_sucursal)
	-- 			references bot_empresas(za_empresa,za_sucursal),
	unique(za_empresa,za_sucursal,za_usuario)
);

drop table if exists bot_modulos;

create table bot_modulos(
	za_modulo smallint not null,
    za_empresa smallint not null,
    nombre_modulo varchar(100) not null,
    url_ico varchar(100) not null,
    url_modulo varchar(200) not null,
    activo tinyint,
    constraint PK_bot_modulos primary key(za_empresa,za_modulo),
    constraint FK_modulos_bot_empresas foreign key(za_empresa)
				references bot_empresas(za_empresa),
	unique(za_empresa,za_modulo)
);

drop table if exists bot_menus_modulos;

create table bot_menus_modulos(
	za_menu smallint not null,
    za_modulo smallint not null,
    za_empresa smallint not null,
    nombre_menu varchar(100) not null,
    url_ico varchar(100) not null,
    activo tinyint,
    constraint PK_bot_menus_modulos primary key(za_empresa,za_modulo,za_menu),
    constraint FK_bot_menus_bot_modulos foreign key(za_empresa,za_modulo)
				references bot_modulos(za_empresa,za_modulo),
	unique(za_empresa,za_modulo,za_menu)
);

drop table if exists bot_opciones_menus;

create table bot_opciones_menus(
	za_op_menu smallint not null,
    za_menu smallint not null,
    za_modulo smallint not null,
    za_empresa smallint not null,
    nombre_opcion varchar(150) not null,
    url_opcion varchar(200) not null,
    ico_url varchar(100) not null,
    activo tinyint,
    constraint PK_bot_opciones_menus primary key(za_empresa,za_modulo,za_menu,za_op_menu),
    constraint FK_bot_opciones_bot_menus foreign key(za_empresa,za_modulo,za_menu)
				references bot_menus_modulos(za_empresa,za_modulo,za_menu),
	unique(za_empresa,za_modulo,za_menu,za_op_menu)
);

drop table if exists bot_accesos_usuarios;

create table bot_accesos_usuarios(
	za_acceso smallint not null,
    za_op_menu smallint not null,
    za_menu smallint not null,
    za_modulo smallint not null,
    za_empresa smallint not null,
    za_usuario int not null,
    ver tinyint not null default 0,
    modificar tinyint not null default 0,
    eliminar tinyint not null default 0,
    imprimir tinyint not null default 0,
    activo tinyint not null default 1,
    constraint PK_bot_accesos_usuarios primary key(za_usuario,za_empresa,za_modulo,za_menu,za_op_menu,za_acceso),
    constraint FK_bot_accesos_bot_opciones foreign key(za_empresa,za_modulo,za_menu,za_op_menu)
				references bot_opciones_menus(za_empresa,za_modulo,za_menu,za_op_menu),
	unique(za_usuario,za_empresa,za_modulo,za_menu,za_op_menu,za_acceso)
);

drop user if exists 'usuario'@'localhost';
grant select, insert, update, delete on qpos.* to 'usuario'@'localhost' identified by 'usuario';
grant execute on *.* to 'usuario'@'localhost';

insert into bot_empresas values(1,'Central','',0,0,'','','','',now(),1);
insert into bot_sucursales_empresas values(1,1,'Administración',1,1,1,0,'','','',now(),1);
insert into bot_usuarios values(1,1,1,'Admin',convert('Admin',binary),'Admin',0,'AD',now(),1);

-- Estas incersiones sirven para que el usuario admin pueda registrar la empresa real en el sistema
insert into bot_modulos values(1,1,'Configuraciones','ico_config.png','qpos/configuraciones',1);
insert into bot_menus_modulos values(1,1,1,'Mi Empresa','ico_mi_empresa.png',1);
insert into bot_opciones_menus values(1,1,1,1,'Registro empresarial','qpos/configuraciones/registro.html','ico_registro.png',1);
insert into bot_accesos_usuarios values(1,1,1,1,1,1,1,1,1,1,1);
-- Las urls pueden ser modificadas para dar la dirección correcta


drop table if exists bot_documentos;

create table bot_documentos(
	za_doc smallint not null,
    za_empresa smallint not null,
    za_sucursal smallint not null,
    za_tipo_tabla smallint not null,
    za_tipo_dato smallint not null,
    url_doc varchar(900) not null,
    activo tinyint not null default 1,
    constraint PK_bot_documentos primary key(za_tipo_dato,za_tipo_tabla,za_sucursal,za_empresa,za_doc),
    unique(za_tipo_dato,za_tipo_tabla,za_sucursal,za_empresa,za_doc)
);