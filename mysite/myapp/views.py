from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import SugerenciaForm

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def myapp(request):
    data = {
        'form': SugerenciaForm(),
        'LANGUAGE_CODE': get_language(),
    }
    if request.method =="POST":
        formulario = SugerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Sugerencia guardada"
        else:
            data["form"] = formulario
    return render(request, 'home.html', data,)


def change_language(request):
    lang_code = request.GET.get('lang', 'en')
    if lang_code in dict(settings.LANGUAGES).keys():
        translation.activate(lang_code)
        response = redirect('/')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    else:
        return redirect('/')
