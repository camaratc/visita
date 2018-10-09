from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse('Hello Index')

def cadastro_pessoas(request):
    return HttpResponse('Cadastro Pessoas')

def cadastro_visitas(request):
    return HttpResponse('Cadastro Visitas')
