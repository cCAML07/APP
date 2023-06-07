# Create your views here.
import persona
from django.http import HttpResponse
from django.template import loader

from personas.models import Persona


def bienvenida(request):
   # return HttpResponse('<!DOCTYPE html><html><head></head><title>PROYECTO</title><body><p>Hola Universidad de Guaayquil</p></body></html>')
    pagina = loader.get_template('saludo.html')
    return HttpResponse(pagina.render())

def hola(request, nombre):
    apellido= request.GET["apellido"]
    nivel=request.GET["nivel"]
    curso=request.GET["curso"]
    pagina = loader.get_template('saludo.html')
    nombreCompleto = nombre + " " + apellido
    datos = {'nombre': nombreCompleto, 'curso':curso, 'nivel':nivel}
    return HttpResponse(pagina.render(datos, request))

def edad(request,edad):
    pass
    pagina = loader.get_template('edad.html')
    mensaje={'edad' : edad}
    return HttpResponse(pagina.render(mensaje, request))

def mostrar_personas(request):
    cantidad_personas = Persona.objects.count()

    personas = Persona.objects.all().values()
    datos= {'cantidad': cantidad_personas, 'personas': personas}
    pagina = loader.get_template('personas.html')


    return HttpResponse(pagina.render(datos,request))

