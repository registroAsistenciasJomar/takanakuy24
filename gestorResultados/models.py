from django.db import models

# Create your models here.

class Canto(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    jurado = models.CharField('Jurado Calificador', max_length=50, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    criterio_1 = models.IntegerField('Crit 01', null=False, blank=False)
    criterio_2 = models.IntegerField('Crit 02', null=False, blank=False)
    criterio_3 = models.IntegerField('Crit 03', null=False, blank=False)
    criterio_4 = models.IntegerField('Crit 04', null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"

class Baile(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    jurado = models.CharField('Jurado Calificador', max_length=50, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    criterio_1 = models.IntegerField('Crit 01', null=False, blank=False)
    criterio_2 = models.IntegerField('Crit 02', null=False, blank=False)
    criterio_3 = models.IntegerField('Crit 03', null=False, blank=False)
    criterio_4 = models.IntegerField('Crit 04', null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"

class PlayBack(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    jurado = models.CharField('Jurado Calificador', max_length=50, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    criterio_1 = models.IntegerField('Crit 01', null=False, blank=False)
    criterio_2 = models.IntegerField('Crit 02', null=False, blank=False)
    criterio_3 = models.IntegerField('Crit 03', null=False, blank=False)
    criterio_4 = models.IntegerField('Crit 04', null=False, blank=False)
    criterio_5 = models.IntegerField('Crit 05', null=False, blank=False)
    criterio_6 = models.IntegerField('Crit 06', null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"

class Conocimientos(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"

class Juegos(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    criterio_1 = models.IntegerField('Juego 01', null=False, blank=False)
    criterio_2 = models.IntegerField('Juego 02', null=False, blank=False)
    criterio_3 = models.IntegerField('Juego 03', null=False, blank=False)
    criterio_4 = models.IntegerField('Juego 04', null=False, blank=False)
    criterio_5 = models.IntegerField('Juego 05', null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"

class Barras(models.Model):
    id_resultado = models.AutoField('Resultado ID', primary_key=True, null=False, blank=False)
    jurado = models.CharField('Jurado Calificador', max_length=50, null=False, blank=False)
    grado = models.CharField('Grado', max_length=25, null=False, blank=False)
    seccion = models.CharField('Sección', max_length=2, null=False, blank=False)
    criterio_1 = models.IntegerField('Crit 01', null=False, blank=False)
    criterio_2 = models.IntegerField('Crit 02', null=False, blank=False)
    criterio_3 = models.IntegerField('Crit 03', null=False, blank=False)
    criterio_4 = models.IntegerField('Crit 04', null=False, blank=False)
    criterio_5 = models.IntegerField('Crit 05', null=False, blank=False)
    criterio_6 = models.IntegerField('Crit 06', null=False, blank=False)
    criterio_7 = models.IntegerField('Crit 07', null=False, blank=False)
    calificacion = models.IntegerField('Calificación Final', null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.grado} {self.seccion}: {self.calificacion}"
