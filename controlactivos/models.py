# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActivosFijos(models.Model):
    id_activo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=120)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_area = models.ForeignKey('Areas', models.DO_NOTHING, db_column='id_area')
    id_categoria_activos = models.ForeignKey('CategoriasActivos', models.DO_NOTHING, db_column='id_categoria_activos')
    estado = models.CharField(max_length=13)
    ficha_tecnica = models.TextField(blank=True, null=True)
    precio_lista = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    numero_serie = models.CharField(max_length=160, blank=True, null=True)
    etiquetas = models.JSONField(blank=True, null=True)
    creado_en = models.DateTimeField()
    actualizado_en = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activos_fijos'


class Areas(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    id_departamento = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='id_departamento')

    class Meta:
        managed = False
        db_table = 'areas'


class CategoriasActivos(models.Model):
    id_categoria_activos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'categorias_activos'


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_activo = models.ForeignKey(ActivosFijos, models.DO_NOTHING, db_column='id_activo')
    id_incidencia = models.ForeignKey('Incidencias', models.DO_NOTHING, db_column='id_incidencia', blank=True, null=True)
    id_usuario_tecnico = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_tecnico', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    fecha_diagnostico = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField()
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial'


class Incidencias(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    descripcion_problema = models.TextField()
    estado = models.CharField(max_length=10)
    tipo_incidencia = models.CharField(max_length=11)
    origen_incidencia = models.CharField(max_length=13)
    prioridad = models.CharField(max_length=7)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_activo = models.ForeignKey(ActivosFijos, models.DO_NOTHING, db_column='id_activo')
    creada_en = models.DateTimeField()
    cerrada_en = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidencias'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=180)
    rol = models.CharField(max_length=11)
    contrasena_hash = models.CharField(max_length=255)
    creado_en = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuarios'
