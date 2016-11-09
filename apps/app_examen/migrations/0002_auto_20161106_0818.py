# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='id',
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='pregunta',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
