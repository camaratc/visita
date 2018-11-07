from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.db import connection
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime

from .models import Pessoa
from .models import Visita

from .forms import PessoaForm
from .forms import VisitaForm
from .forms import FiltroHistoricoForm

@login_required
def index(request):
    return render(request, 'home.html', {})

@login_required
def cadastro_pessoas(request, edit=False):
    if edit:
        editar = get_object_or_404(Pessoa, pk=edit.pk)
    else:
        editar = None

    if request.method == 'POST':      
        form = PessoaForm(request.POST, request.FILES, instance=editar)

        if form.is_valid():
            pessoa = form.save(commit = False)
            pessoa.dataCadastro = timezone.now()

            pessoa.save()

            return redirect('cadastro:cadastro_visitas')
    else:
        form = PessoaForm(instance=editar)

    return render(request, 'cadastrar-pessoas.html', {'form': form})

@login_required
def listar_pessoas(request):
    lista_pessoas = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(lista_pessoas, 15)
    page = request.GET.get('page')
    pessoas = paginator.get_page(page)

    return render(request, 'lista-pessoas.html', {'pessoas': pessoas})

@login_required
def perfil_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return render(request, 'pessoa-detalhes.html', {'pessoa': pessoa})

@login_required
def editar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    return cadastro_pessoas(request, pessoa)

@login_required
def api_pessoas(request):
    lista = Pessoa.objects.all()
    lista = serializers.serialize('json', lista)
    return HttpResponse(lista, content_type="application/json")

@login_required
def cadastro_visitas(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)

        if form.is_valid():
            visita = form.save(commit = False)
            visita.data = timezone.now()
            visita.horarioEntrada = timezone.now()
            visita.horarioSaida = None

            visita.save()

            return redirect('cadastro:cadastro_visitas')
    else:
        form = VisitaForm()

    visitas = Visita.objects.filter(horarioSaida=None).order_by('-horarioEntrada')
    nomes = []

    context = {
        'form': form,
        'visitas': visitas,
        'nomes': nomes
    }

    return render(request, 'cadastrar-visitas.html', context)

@login_required
def historico_visitas(request):
    if request.method == "GET":
        form = FiltroHistoricoForm(request.GET)

        if form.is_valid():
            if(form.cleaned_data['data_inicial'] and form.cleaned_data['data_final']):
                visitas_lista = Visita.objects.filter(
                    (
                        (
                            Q(pessoa__nome__icontains=form.cleaned_data['busca']) |
                            Q(setor__icontains=form.cleaned_data['busca'])
                        ) &
                        Q(data__range=(
                            form.cleaned_data['data_inicial'],
                            form.cleaned_data['data_final'])
                        )
                    ),
                ).order_by('-data', '-horarioEntrada')
            elif(form.cleaned_data['data_inicial'] and not form.cleaned_data['data_final']):
                visitas_lista = Visita.objects.filter(
                    (
                        (
                            Q(pessoa__nome__icontains=form.cleaned_data['busca']) |
                            Q(setor__icontains=form.cleaned_data['busca'])
                        ) &
                        Q(data__gte=form.cleaned_data['data_inicial'])
                    ),
                ).order_by('-data', '-horarioEntrada')
            elif(not form.cleaned_data['data_inicial'] and form.cleaned_data['data_final']):
                visitas_lista = Visita.objects.filter(
                    (
                        (
                            Q(pessoa__nome__icontains=form.cleaned_data['busca']) |
                            Q(setor__icontains=form.cleaned_data['busca'])
                        ) &
                        Q(data__lte=form.cleaned_data['data_final'])
                    ),
                ).order_by('-data', '-horarioEntrada')
            else:
                if(form.cleaned_data['busca']):
                    visitas_lista = Visita.objects.filter(
                        Q(pessoa__nome__icontains=form.cleaned_data['busca']) |
                        Q(setor__icontains=form.cleaned_data['busca'])
                    ).order_by('-data', '-horarioEntrada')
                else:
                    visitas_lista = Visita.objects.all().order_by('-data', '-horarioEntrada')
    else:
        form = FiltroHistoricoForm()
    
    paginator = Paginator(visitas_lista, 10)

    page = request.GET.get('page')
    visitas = paginator.get_page(page)

    return render(request, 'historico-visitas.html', {'visitas': visitas, 'form': form})

@login_required
def visita_detalhes(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    return render(request, 'visita-detalhes.html', {'visita': visita})

@login_required
def confirmar_saida(request, pk):
    visita = Visita.objects.filter(pk=pk).update(horarioSaida=timezone.now())
    return historico_visitas(request)
