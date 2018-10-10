from django.shortcuts import render, redirect
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
import datetime

from .models import Pessoa
from .forms import PessoaForm

def index(request):
    return HttpResponse('Hello Index')

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
