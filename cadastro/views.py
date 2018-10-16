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
    return render(request, 'home.html', {})

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

    return render(request, "cadastrar-pessoas.html", {'form': form})

def cadastro_visitas(request):
    return render(request, 'cadastrar-visitas.html', {})
