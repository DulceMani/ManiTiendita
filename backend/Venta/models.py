from django.db import models

class Venta:
    precio_venta = models.FloatField(
        verbose_name="Precio",
        blank=False,
        null=False
    )
