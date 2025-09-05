from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    return render(request,'gestionCursos.html',{'cursos':cursos})

def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['txtCredito']
    
    curso = Curso.objects.create(codigo = codigo, nombre = nombre, credito = credito)
    return redirect('/')

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()
    return redirect('/')

def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request,'edicionCurso.html',{'curso':curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['txtCredito']
    
    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.credito = credito
    curso.save()
    
    return redirect('/') # Redirecciona a la pagina de inicio.
    