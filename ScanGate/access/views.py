from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Registros
from django.urls import reverse
from django.db import transaction
import time
import base64

def access(request):
    return render(request, 'access/index.html')

def perfil(request, codigo_barras):
    hora_actual = [time.asctime(time.localtime())]

    with transaction.atomic():
        persona = get_object_or_404(Registros, codigo_barras=codigo_barras)
        persona_horas = eval(persona.hora_entrada)

        horas_totales = persona_horas + hora_actual

        Registros.objects.filter(codigo_barras=codigo_barras).update(hora_entrada=horas_totales)    

    if request.method == 'POST':
        nueva_foto = request.FILES.get('nueva_foto')
        if nueva_foto:
            persona.foto = nueva_foto.read() 
            persona.save()
            return redirect('/')

    # Si no se habia registrado antes

    if persona.foto == "S/N":
        context = {
            'nombre': persona.nombre,
            'ciudad_estado': persona.ciudad_estado,
            'correo': persona.correo,
            'empresa': persona.empresa,
            'num_telefono': persona.num_telefono,
            'codigo_barras': persona.codigo_barras,
            'hora_entrada': hora_actual[0],
        }
    else:
        foto = base64.b64encode(persona.foto).decode()
    # Ya se habia registrado
        context = {
            'nombre': persona.nombre,
            'ciudad_estado': persona.ciudad_estado,
            'correo': persona.correo,
            'empresa': persona.empresa,
            'num_telefono': persona.num_telefono,
            'codigo_barras': persona.codigo_barras,
            'hora_entrada': 0,
            'ultima_hora': persona_horas[-1],
            'foto': foto
        }



    return render(request, 'access/perfil.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'access/login.html', {'error': 'Invalid username or password'})
    return render(request, 'access/login.html')
