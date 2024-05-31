from django.db import models

class Registros(models.Model):
    codigo_barras = models.CharField(max_length=50, default='S/N')
    nombre = models.CharField(max_length=50, default='S/N')
    num_telefono = models.CharField(max_length=50, default='S/N')
    correo = models.CharField(max_length=50, default='S/N')
    empresa = models.CharField(max_length=50, default='S/N')
    ciudad_estado = models.CharField(max_length=50, default='S/N')
    hora_entrada = models.TextField(default="[]")
    foto = models.BinaryField()

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
