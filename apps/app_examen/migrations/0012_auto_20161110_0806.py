# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0011_auto_20161110_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='materi',
            field=models.CharField(max_length=100),
        ),
    ]
