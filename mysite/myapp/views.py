from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def myapp (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
