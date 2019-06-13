from django.shortcuts import render
from django.http import HttpResponse
from configuraciones.models import bot_modulos, bot_opciones_modulo
# Create your views here.

def config_empresa(request):
		#return HttpResponse('Hello Word')
		modulos = bot_modulos.objects.all()
		opciones = bot_opciones_modulo.objects.all()
		return render(request, 'base.html', {'modulos': modulos, 'opciones': opciones})