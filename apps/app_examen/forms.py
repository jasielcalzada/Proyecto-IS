from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import Respuesta,Preguntas

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=64)
    mail=forms.CharField(max_length=50)

class UserFormAlumno(UserCreationForm):
    #mail = forms.CharField()
    #name = forms.CharField(max_length=64)
    n_control = forms.CharField(max_length=64)
    materi = forms.CharField(max_length=64)


#Coregir
class Preguntas_form(forms.Form):
    pregunta = forms.CharField(max_length=64)
    #nivel = (('Facil','Facil'),('Intermedio','Intermedio'),('Dificil','Dificil'))
    dificultad = forms.CharField()
    valor = forms.IntegerField()

class respuestas_form(forms.Form):
    opcion = forms.CharField(max_length=64)
    pregun = forms.CharField(max_length=64)
    #pregun = forms.ChoiceField()#queryset=Preguntas.objects.filter(id = id))
