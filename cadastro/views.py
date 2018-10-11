from django.shortcuts import render, redirect
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.db import connection
import datetime
import simplejson

from .models import Pessoa
from .forms import PessoaForm

def index(request):
    return HttpResponse('Hello Index')

def get_estados(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM localidades_estado')

    data = []
    for item in cursor:
        data.append(item)

    json = simplejson.dumps(data)
    return HttpResponse(json, content_type='application/json')

def get_cidades(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM localidades_cidade')

    data = []
    for item in cursor:
        data.append(item)

    json = simplejson.dumps(data)
    return HttpResponse(json, content_type='application/json')

def cadastro_pessoas(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit = False)
            pessoa.dataCadastro = timezone.now()

            pessoa.save()

            return redirect('cadastro:index')
    else:
        form = PessoaForm()

    return render(request, "pessoas.html", {'form': form})

def cadastro_visitas(request):
    return HttpResponse('Cadastro Visitas')
