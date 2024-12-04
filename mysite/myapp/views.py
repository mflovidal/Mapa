from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import SugerenciaForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from .forms import CustomLoginForm, SugerenciaForm
from .models import Event, Sugerencias
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.http import JsonResponse
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

def index(request):
    """Vista para la página principal con el calendario."""
    events = Event.objects.all()
    events_data = [
        {
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'description': event.description
        }
        for event in events
    ]
    return render(request, 'home.html', {'events': events_data})

def view_calendar(request):
    """Vista para mostrar el calendario sin permitir la edición."""
    events = Event.objects.all()
    events_data = [
        {
            'id': event.id,
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'description': event.description
        }
        for event in events
    ]
    return render(request, 'view_calendar.html', {'events': events_data})

#@login_required
@permission_required('myapp.view_sugerencias', raise_exception=True)
@permission_required('myapp.change_sugerencias', raise_exception=True)
def edit_calendar(request):
    events = Event.objects.all()
    events_data = [
        {
            'id': event.id,
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'description': event.description
        }
        for event in events
    ]
    return render(request, 'edit_calendar.html', {'events': events_data})

@permission_required('myapp.view_sugerencias', raise_exception=True)
@permission_required('myapp.change_sugerencias', raise_exception=True)
@csrf_exempt
def add_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        event = Event.objects.create(
            title=title,
            start_time=start_time,
            end_time=end_time
        )
        return JsonResponse({
            'event': {
                'id': event.id,
                'title': event.title,
                'start': event.start_time.isoformat(),
                'end': event.end_time.isoformat(),
                'description': event.description
            }
        })

@permission_required('myapp.view_sugerencias', raise_exception=True)
@permission_required('myapp.change_sugerencias', raise_exception=True)
@csrf_exempt
def update_event(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        title = request.POST.get('title')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        event = Event.objects.get(id=event_id)
        event.title = title
        event.start_time = start_time
        event.end_time = end_time
        event.save()

        return JsonResponse({
            'event': {
                'id': event.id,
                'title': event.title,
                'start': event.start_time.isoformat(),
                'end': event.end_time.isoformat(),
                'description': event.description
            }
        })
@permission_required('myapp.view_sugerencias', raise_exception=True)
@permission_required('myapp.change_sugerencias', raise_exception=True)
@csrf_exempt
def delete_event(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        event = Event.objects.get(id=event_id)
        event.delete()

        return JsonResponse({'status': 'success'})
    
@permission_required('myapp.view_sugerencias', raise_exception=True)
@permission_required('myapp.change_sugerencias', raise_exception=True)
def ver_sugerencias(request):
    buscar = request.GET.get('q', '')
    estado = request.GET.get('estado', '')
    if buscar and estado:
        sugerencias = Sugerencias.objects.filter(sugerencia__icontains=buscar, estado=estado).order_by('-fecha_creacion')
    elif buscar:
        sugerencias = Sugerencias.objects.filter(sugerencia__icontains=buscar).order_by('-fecha_creacion')
    elif estado:
        sugerencias = Sugerencias.objects.filter(estado=estado).order_by('-fecha_creacion')
    else:
        sugerencias = Sugerencias.objects.all().order_by('-fecha_creacion')

    if request.method == 'POST' and 'estado' in request.POST:
        sugerencia_id = request.POST.get('sugerencia_id')
        estado = request.POST.get('estado')
        try:
            sugerencia = Sugerencias.objects.get(id=sugerencia_id)
            sugerencia.estado = estado
            sugerencia.save()
            return redirect('ver_sugerencias')
        except Sugerencias.DoesNotExist:
            pass
    return render(request, 'ver_sugerencias.html', {
        'sugerencias': sugerencias,
        'buscar': buscar,
        'estado': estado,
    })
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ver_sugerencias')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('/')