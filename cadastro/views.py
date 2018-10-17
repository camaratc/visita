from django.shortcuts import render, redirect
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.db import connection
import datetime
import simplejson

from .models import Pessoa
from .models import Visita

from .forms import PessoaForm
from .forms import VisitaForm

def index(request):
    return render(request, 'home.html', {})

def cadastro_pessoas(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit = False)
            pessoa.dataCadastro = timezone.now()

            pessoa.save()

            return redirect('cadastro:index')
    else:
        form = PessoaForm()

    return render(request, 'cadastrar-pessoas.html', {'form': form})

def cadastro_visitas(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)

        if form.is_valid():
            visita = form.save(commit = False)
            visita.data = timezone.now()
            visita.horarioEntrada = timezone.now()
            visita.horarioSaida = None

            visita.save()

            return redirect('cadastro:index')
    else:
        form = VisitaForm()

    return render(request, 'cadastrar-visitas.html', {'form': form})

def historico_visitas(request):
    visitas = Visita.objects.all().order_by('-horarioEntrada')[:10:1]

    print(visitas)

    return render(request, 'historico-visitas.html', {'visitas': visitas})
