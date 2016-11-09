# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0004_auto_20161109_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
