from django.shortcuts import render
from django.http import HttpResponse

def myapp(request):
    return HttpResponse("Hello World!")

# Create your views here.
