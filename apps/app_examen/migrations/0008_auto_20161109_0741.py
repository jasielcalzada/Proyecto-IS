# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0007_auto_20161109_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='name',
            field=models.CharField(default=b'Alumno#', max_length=64, null=True, blank=True),
        ),
    ]
