from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
# Create your models here.
class Materia(models.Model):
    materia = models.CharField(max_length=64,null=True)
    serie = models.SlugField(max_length=64,primary_key=True)
    profesor = models.CharField(max_length=64,null=True)

    def __unicode__(self):
        return '%s'%(self.serie)
    def __str__(self):
        return self.serie

class Profesor(models.Model):
    user_perfil = models.OneToOneField(User, related_name="profile")
    mail = models.EmailField()
    name = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64,null = True,default="profesor")

    def __unicode__(self):
        return '%s'%(self.user_perfil)


class Alumno(models.Model):
    user_perfil = models.OneToOneField(User, related_name="profile_a")
    mail = models.EmailField(null=True,blank=True,default="correo@correo")
    name = models.CharField(max_length=64,null=True,blank=True,default="Alumno#")
    n_control = models.SlugField(max_length=64,primary_key=True,null=False)
    materi = models.CharField(max_length=100)
    categoria = models.CharField(max_length=64,null=True,default="alumno")

    def __unicode__(self):
        return '%s'%(self.n_control)


#NO USAR ESTE

#
class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200,primary_key=True)
    nivel = (('Facil','Facil'),('Intermedio','Intermedio'),('Dificil','Dificil'))
    dificultad = models.CharField(max_length=64,choices=nivel)
    valor = models.PositiveIntegerField( validators=[MinValueValidator(1),MaxValueValidator(100)])
    s = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'))
    semestre = models.CharField(max_length=64,null = True,choices=s)
    materia = models.CharField(max_length=64,null=True)
    def __unicode__(self):
        return '%s'%(self.pregunta)

class Respuesta(models.Model):
    opcion  = models.CharField(max_length=200,blank=True)
    correct = models.BooleanField(default=False,blank=True)
    pregun  = models.ForeignKey(Preguntas,null=True, blank=True, default=None)

    def __unicode__(self):
        return self.opcion

#class Examen(models.Model):
#    materia = models.ForeignKey(Materia,null=True,on_delete=models.CASCADE,db_index=True)
#    profesor = models.ForeignKey(Profesor,null=True)
#    alumno = models.ForeignKey(Alumno,null=True)
#    unidad = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(7)],null=True)
#    pregun = models.ForeignKey(Preguntas)
#    respue = models.ForeignKey(Respuesta)
#    def __unicode__(self):
#        return '%s %s %s %d %s %s'%(self.materia,self.profesor.name,self.alumno.name,self.unidad,self.pregun,self.respue)

class examen(models.Model):
    materia = models.ForeignKey(Materia)
    profesor = models.ForeignKey(Profesor)
    alumno = models.ForeignKey(Alumno)
    unidad = models.IntegerField()
    pregunta = models.ForeignKey(Preguntas,null=True)
    respuesta = models.ForeignKey(Respuesta,null=True)
    def __unicode__(self):
        return '%s %s %s %d %s %s'%(self.materia,self.profesor,self.alumno,self.unidad,self.pregunta,self.respuesta)
    def __str__(self):
        return self.materia,self.profesor,self.alumno,self.unidad,self.pregunta,self.respuesta

class extra(models.Model):
    a = models.IntegerField()

    def __unicode__(self):
        return self.a