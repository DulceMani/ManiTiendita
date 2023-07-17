from django.db import models
from datetime import datetime


class Categoria(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre",
        blank=False,
        null=False,
        max_length=100
    )
    descripcion = models.TextField(
        verbose_name="Descripción",
        max_length=500
    )
    fecha_reg = models.DateTimeField(
        default=datetime.now()
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Marca(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre",
        blank=False,
        null=False,
        max_length=100
    )
    fecha_reg = models.DateTimeField(
        default=datetime.now()
    )

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class UnidadMedida(models.Model):
    nombre_largo = models.CharField(
        verbose_name="Nombre",
        blank=False,
        null=False,
        max_length=100
    )
    nombre_corto = models.CharField(
        verbose_name="Nombre corto",
        blank=False,
        null=False,
        max_length=10
    )

    class Meta:
        verbose_name = "UnidadMedida"
        verbose_name_plural = "Unidades de Medida"


class Producto(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre",
        blank=False,
        null=False,
        max_length=100)
    descripcion = models.TextField(
        verbose_name="Descripción de Producto",
        max_length=500
    )
    precio_compra = models.FloatField(
        verbose_name="Precio de Compra",
        blank=False,
        null=False
    )
    precio_venta = models.FloatField(
        verbose_name="Precio de Venta",
        blank=False,
        null=False
    )
    existencias = models.FloatField(
        verbose_name="Nombre",
        blank=False,
        null=False,
        default=0
    )

    fecha_reg = models.DateTimeField(
        default=datetime.now()
    )
    unidad_medida = models.ForeignKey(
        UnidadMedida,
        on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"