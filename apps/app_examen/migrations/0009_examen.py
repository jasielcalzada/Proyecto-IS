# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0008_auto_20161109_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.IntegerField()),
                ('alumno', models.ForeignKey(to='app_examen.Alumno')),
                ('materia', models.ForeignKey(to='app_examen.Materia')),
                ('pregunta', models.ForeignKey(to='app_examen.Respuesta')),
                ('profesor', models.ForeignKey(to='app_examen.Profesor')),
            ],
        ),
    ]
