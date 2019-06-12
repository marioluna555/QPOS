from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def config_empresa(request):
		#return HttpResponse('Hello Word')
		return render(request, 'base.html')