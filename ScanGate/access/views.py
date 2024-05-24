from django.shortcuts import render, get_object_or_404, redirect
from .models import Registros
import cv2
from pyzbar import pyzbar
from django.db import transaction
from django.utils import timezone
from django.http import HttpResponseBadRequest
def access(request):
    return render(request, 'access/index.html')

def perfil(request, codigo_barras):
    with transaction.atomic():
        Registros.objects.filter(codigo_barras=codigo_barras).update(hora_entrada=timezone.now())
        persona = get_object_or_404(Registros, codigo_barras=codigo_barras)

    if request.method == 'POST':
        nueva_foto = request.FILES.get('nueva_foto')
        if nueva_foto:
            persona.foto = nueva_foto.read() 
            persona.save()
            return redirect('/')

    context = {
        'nombre': persona.nombre,
        'ciudad_estado': persona.ciudad_estado,
        'correo': persona.correo,
        'empresa': persona.empresa,
        'num_telefono': persona.num_telefono,
        'codigo_barras': persona.codigo_barras,
        'hora_entrada': persona.hora_entrada,
    }

    return render(request, 'access/perfil.html', context)
