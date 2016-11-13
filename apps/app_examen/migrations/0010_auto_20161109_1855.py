# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0009_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='respuesta',
            field=models.ForeignKey(to='app_examen.Respuesta', null=True),
        ),
        migrations.AlterField(
            model_name='examen',
            name='pregunta',
            field=models.ForeignKey(to='app_examen.Preguntas', null=True),
        ),
    ]
