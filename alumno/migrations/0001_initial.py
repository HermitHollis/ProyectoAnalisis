# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=2, default='M', choices=[('M', 'Mascuilino'), ('F', 'Femenino')])),
                ('descripcion_de_alumno', models.TextField()),
                ('matricula', models.CharField(max_length=9)),
                ('grupo', models.CharField(max_length=3)),
                ('ciclo_escolar', models.CharField(max_length=6)),
                ('plan_curricular', models.CharField(max_length=10)),
                ('acreditado', models.BooleanField(default=False)),
            ],
        ),
    ]
