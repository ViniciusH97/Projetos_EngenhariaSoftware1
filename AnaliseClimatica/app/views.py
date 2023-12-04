from django.shortcuts import render, redirect
from app.forms import *
from . models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from urllib.parse import unquote

def paises(request):
    pais = {
        'pais': pais.objects.all()
    }
    return render(request, 'paises/paises.html', pais)


def adm(request):
    return render(request, 'adm/adm.html')


def consultar_causa(request):
    return render(request, 'causa/consultar_causa.html')


def buscar_causas(request):
    estado_nome = request.GET.get('estado_id')
    estado_nome_decoded = unquote(estado_nome)
    estado = get_object_or_404(Estado, nome=estado_nome_decoded)
    
    mapa_brasil_src = f'/static/mapa_brasil.jpeg'

    causas = estado.causas.all()


    data = {'causas': [causa.to_dict_json() for causa in causas], 'mapa_brasil_src': mapa_brasil_src}
    return JsonResponse(data)
