from django.shortcuts import render
from django.http import HttpResponse

from personas.models import Persona

# Create your views here.
def bienvenido(request):
  no_personas = Persona.objects.count()
  # personas = Persona.objects.all()
  personas = Persona.objects.order_by('id')     # Ordenamiento ascendente
  # personas = Persona.objects.order_by('-id')  # Ordenamiento descendente
  # personas = Persona.objects.order_by('nombre', '-id')     # Ordenamiento multiple
  
  return render(request, 'bienvenido.html', { 'no_personas': no_personas, 'personas': personas })