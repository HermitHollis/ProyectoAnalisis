# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='imagen',
            field=models.ImageField(verbose_name='Imagen alumno', null=True, blank=True, upload_to='Proyecto/images/'),
        ),
    ]
