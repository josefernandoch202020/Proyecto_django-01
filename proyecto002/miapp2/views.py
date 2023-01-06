from django.shortcuts import render,HttpResponse

# Create your views here.

def inicio(request):
        return render(request,'inicio.html')

def cursos(request):
        mensaje="Curso registrado"
        return HttpResponse(mensaje)

def crear_curso(request):
        mensaje="Curso creado"
        return HttpResponse(mensaje)

def carreras(request):
        mensaje="Listado de cursos"
        return HttpResponse(mensaje)

def crear_carrera(request):
        mensaje="Curso creado"
        return HttpResponse(mensaje)