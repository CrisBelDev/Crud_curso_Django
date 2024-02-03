from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
# Create your views here.

# listado__________________________
def home(request):
    cursosListados = Curso.objects.all() # consulta sql trae todos los cursos listados
    messages.success(request,'Cursos Listados!')
    return render(request, "gestionCursos.html",{"cursos":cursosListados})
# fin listado_______________________

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso = Curso.objects.create(codigo = codigo, nombre=nombre, creditos=creditos)
    messages.success(request,'Curso registrado!')
    return redirect('/')

def eliminarCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Cursos eliminado!')
    return redirect('/')

def edicionCurso(request,codigo):
     curso=Curso.objects.get(codigo=codigo)
     return render(request,'edicionCurso.html',{"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request,'Cursos actualizado!')
    return redirect('/')