# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0002_auto_20161106_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='materi',
            field=models.CharField(max_length=64),
        ),
    ]
