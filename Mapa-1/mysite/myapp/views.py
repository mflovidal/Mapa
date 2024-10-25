from django.shortcuts import render, redirect, get_object_or_404
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def myapp(request):
    return render(request, 'home.html', {
        'LANGUAGE_CODE': get_language(),
    })

def change_language(request):
    lang_code = request.GET.get('lang', 'en')
    if lang_code in dict(settings.LANGUAGES).keys():
        translation.activate(lang_code)
        response = redirect('/')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    else:
        return redirect('/')
# los marcadores 
#from .models import Marcador
#from .formulario import MarcadorForm

#def agregar_marcador(request):
    if request.method == 'POST':
        form = MarcadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_marcadores')
    else:
        form = MarcadorForm()
    return render(request, 'agregar_marcador.html', {'form': form})

#def editar_marcador(request, id):
    marcador = get_object_or_404(Marcador, id=id)
    if request.method == 'POST':
        form = MarcadorForm(request.POST, request.FILES, instance=marcador)
        if form.is_valid():
            form.save()
            return redirect('listar_marcadores')
    else:
        form = MarcadorForm(instance=marcador)
    return render(request, 'editar_marcador.html', {'form': form})
#el aviso
from django.http import JsonResponse

def casa(request):
    return render(request, 'home.html')

def obtener_mensaje(request):
    mensaje = "¡Hay un evento"
    return JsonResponse({'mensaje': mensaje})
