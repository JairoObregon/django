from django.db import models


class ESTUDIANTE(models.Model):
    CODALU = models.CharField(max_length=200)
    NOMALU = models.CharField(max_length=200)
    APEALU = models.CharField(max_length=200)
    EDAD = models.IntegerField(blank=True, null=True)

class CURSOS(models.Model):
    CODCUR = models.CharField(max_length=200)
    NOMCUR = models.CharField(max_length=200)
    CREDITO = models.IntegerField(blank=True, null=True)


class ALU_CUR(models.Model):
    CODALU = models.ForeignKey(ESTUDIANTE, on_delete = models.CASCADE)
    CODCUR = models.ForeignKey(CURSOS, on_delete = models.CASCADE)
    NOTA = models.DecimalField(max_digits=5, decimal_places=2)

