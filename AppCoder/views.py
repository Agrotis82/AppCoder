from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


# Create your views here.
# def curso(self):

#    curso = Curso(nombre= "Desarrollo Web", camada="19889")
#    curso.save()
#    texto = f"---> Curso: {curso.nombre} Camada: {curso.camada}"
#    return HttpResponse(texto)

def inicio(request):
    return HttpResponse ('vista inicio')

def cursos(request):
    return HttpResponse ('vista cursos')

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return HttpResponse('vista estudiantes')

def entregables(request):
    return HttpResponse('vista entregables')
