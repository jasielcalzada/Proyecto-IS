from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import UserForm, UserFormAlumno, respuestas_form,Preguntas_form
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import Profesor,Materia,Alumno,Preguntas,Respuesta,examen
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
    return render(request,'app_examen/index.html')

def login_view(request):
    return render(request,'app_examen/login.html')

class Signup(FormView):
    template_name = 'app_examen/signup.html'
    form_class = UserForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        user = form.save()
        p = Profesor()
        p.user_perfil = user
        p.name = form.cleaned_data['name']
        p.mail = form.cleaned_data['mail']
        p.save()
        return super(Signup, self).form_valid(form)

class Signup_Alumno(FormView):
    template_name = 'app_examen/Signup_a.html'
    form_class = UserFormAlumno
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        user = form.save()
        p = Alumno()
        p.user_perfil = user
        #p.mail = form.cleaned_data['mail']
        #p.name = form.cleaned_data['name']
        p.n_control = form.cleaned_data['n_control']
        p.materi = form.cleaned_data['materi']
        p.save()
        return super(Signup_Alumno,self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(Signup_Alumno, self).get_context_data(**kwargs)
        #ctx['materias'] = Materia.objects.all()
        return ctx


class register_materia(CreateView):
    template_name = 'app_examen/register_materia.html'
    model = Materia
    fields = ['materia','serie','profesor']
    success_url = reverse_lazy('index_view')

class pregunta(CreateView):
    template_name = 'app_examen/pregunta_respuesta.html'
    model = Preguntas
    fields = ['pregunta','dificultad','valor','semestre','materia']
    success_url = reverse_lazy('register_respuesta')

    def get_context_data(self, **kwargs):
        ctx = super(pregunta, self).get_context_data(**kwargs)
        ctx['materias'] = Materia.objects.all()
        return ctx

class respuesta(CreateView):
    template_name = 'app_examen/respueta_pregunta.html'
    model = Respuesta
    fields = ['opcion','correct','pregun']
    success_url = reverse_lazy('register_respuesta')

    def get_context_data(self, **kwargs):
        ctx = super(respuesta,self).get_context_data(**kwargs)
        ctx['pre'] = Preguntas.objects.all()
        return ctx

def listado_materias(request):
    mate = Materia.objects.all()
    ctx = {'materias':mate,}
    return render(request,'app_examen/app_examen/listado_materias.html',ctx)


#def registroEstudiante(request):
#    form = UserFormAlumno
#    if form.is_valid():
#        user = form.save(commit=False)
#        password = form.cleaned_data.get('password')
#        user.set_password(password)
#        user.save()
#    context = {
#		"form" : form,
#	}
#    return render(request,'app_examen/Signup_a.html', context)

class detalle_materia(DetailView):
    template_name = 'app_examen/detalle_materia.html'
    slug_field = 'serie'
    model = Materia

    def get_context_data(self,**kwargs):
        ctx = super(detalle_materia,self).get_context_data(**kwargs)
        ctx['form'] = UserFormAlumno
        ctx['alumnos'] = Alumno.objects.all()
        #ctx['materia'] = Materia.objects.all()
        return ctx


class Examen_view(CreateView):
    template_name = 'app_examen/generador_examen.html'
    model = examen
    fields = ['materia','profesor','alumno','unidad','pregunta','respuesta']
    success_url = reverse_lazy('index_view')

    def get_context_data(self, **kwargs):
        ctx = super(Examen_view,self).get_context_data(**kwargs)
        ctx['preguntas'] = Respuesta.objects.all()
        return ctx


