# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0003_auto_20161106_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='n_control',
            field=models.SlugField(max_length=64, serialize=False, primary_key=True),
        ),
    ]
