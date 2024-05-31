from django.shortcuts import render, get_object_or_404, redirect
from .models import Registros
from django.db import transaction
import time
import base64

def access(request):
    return render(request, 'access/index.html')

def perfil(request, codigo_barras):
    hora_actual = [time.asctime(time.localtime())]

    with transaction.atomic():
        persona = get_object_or_404(Registros, codigo_barras=codigo_barras)
        print(persona.hora_entrada)
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
