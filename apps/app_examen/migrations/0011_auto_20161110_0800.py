# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0010_auto_20161109_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='materi',
            field=models.ForeignKey(to='app_examen.Materia'),
        ),
    ]
