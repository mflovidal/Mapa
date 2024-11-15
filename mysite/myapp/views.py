from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from django.utils.translation import get_language
from .forms import SugerenciaForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from .models import Event
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

@csrf_exempt
def delete_event(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        event = Event.objects.get(id=event_id)
        event.delete()

        return JsonResponse({'status': 'success'})
    
#def login_view(request):  (para despues)
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['yo']
            password = request.POST['8']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('edit_calendar')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        form = CustomLoginForm()
    return render(request, 'login.html')