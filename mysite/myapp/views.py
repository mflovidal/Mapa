from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import SugerenciaForm, EventoForm
from django.contrib.auth.decorators import login_required
from .models import Evento
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


def calendario_view(request):
    eventos = Evento.objects.all()
    return render(request, 'mysite/calendario.html', {'eventos': eventos})

@login_required
def editar_evento(request, evento_id=None):
    if evento_id:
        evento = Evento.objects.get(id=evento_id)
    else:
        evento = None
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('calendario')
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'mysite/editar_evento.html', {'form': form})