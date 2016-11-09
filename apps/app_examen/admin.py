from django.contrib import admin
from .models import Profesor,Materia,Alumno,Preguntas,Respuesta
# Register your models here.
@admin.register(Profesor)
class Profesor_admin(admin.ModelAdmin):
    list_display = ('id','user_perfil','mail','name','categoria')

@admin.register(Alumno)
class Alumno_admin(admin.ModelAdmin):
    list_display = ('n_control','user_perfil','mail','name','categoria','materi')

@admin.register(Preguntas)
class Preguntas(admin.ModelAdmin):
    list_display = ('pregunta','dificultad','valor','semestre','materia')

@admin.register(Respuesta)
class Respuestas(admin.ModelAdmin):
    list_display = ('id','opcion','correct','pregun')

