from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length = 50)
    Masculino = "M"
    Femenino = "F"
    SEXO_OPCION = (
        (Masculino, "Mascuilino"),
        (Femenino, "Femenino"),
    )
    sexo = models.CharField(max_length = 2, choices = SEXO_OPCION, default = Masculino)
    descripcion_de_alumno = models.TextField()
    matricula = models.CharField(max_length = 9)
    grupo = models.CharField(max_length = 3)
    ciclo_escolar = models.CharField(max_length = 6)
    plan_curricular = models.CharField(max_length = 10)

    acreditado = models.BooleanField(default = False)

    def __str__(self):
        return self.nombre
    ##imagen = models.ImageField()
