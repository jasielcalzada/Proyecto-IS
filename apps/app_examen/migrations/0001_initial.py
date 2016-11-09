# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('n_control', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('categoria', models.CharField(default=b'alumno', max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('materia', models.CharField(max_length=64, null=True)),
                ('serie', models.SlugField(max_length=64, serialize=False, primary_key=True)),
                ('profesor', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=200)),
                ('dificultad', models.CharField(max_length=64, choices=[(b'Facil', b'Facil'), (b'Intermedio', b'Intermedio'), (b'Dificil', b'Dificil')])),
                ('valor', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('semestre', models.CharField(max_length=64, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9')])),
                ('materia', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('categoria', models.CharField(default=b'profesor', max_length=64, null=True)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcion', models.CharField(max_length=200, blank=True)),
                ('correct', models.BooleanField(default=False)),
                ('pregun', models.ForeignKey(default=None, blank=True, to='app_examen.Preguntas', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='materi',
            field=models.ForeignKey(to='app_examen.Materia'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user_perfil',
            field=models.OneToOneField(related_name='profile_a', to=settings.AUTH_USER_MODEL),
        ),
    ]
