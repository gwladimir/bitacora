from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def holaView (request):
    return HttpResponse("Hola Mundo jaja")