from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Olá, mundo! Esta é a minha primeira página Django.")