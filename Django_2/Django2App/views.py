from django.shortcuts import redirect, render
from Django2App.models import ModInscripción
from Django2App.form import FormInscripción

def index(request):
    return render(request, 'index.html')

def Incripcion(request):
    if request.method == 'POST':
        form = FormInscripción(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ListaInscripciones.html')
    else:
        form = FormInscripción()
    return render(request, 'Inscripcion.html', {'form': form})

def ListaInscripciones(request):
    Inscripciones = ModInscripción.objects.all()
    data = {'Inscripciones': Inscripciones}
    return render(request, 'ListaInscripciones.html', data)

def EliminarInscripcion(request, id):
    Inscripcion = ModInscripción.objects.get(id=id)
    Inscripcion.delete()
    return redirect('ListaInscripciones')

def EditarInscripcion(request, id):
    Inscripcion = ModInscripción.objects.get(id=id)
    if request.method == 'POST':
        form = FormInscripción(request.POST, instance=Inscripcion)
        if form.is_valid():
            form.save()
            return redirect('ListaInscripciones')
    else:
        form = FormInscripción(instance=Inscripcion)
    data = {'form': form}
    return render(request, 'EditarInscripcion.html', data)

