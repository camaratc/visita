from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Pessoa
from .models import Visita

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade', 'dataCadastro')
    list_filter = ('estado', 'cidade', ('dataCadastro', DateTimeRangeFilter))
    list_display = ('nome', 'cpf', 'rg', 'endereco','bairro', 'estado', 'cidade', 'dataCadastro')
    ordering = ['nome']

class VisitaAdmin(admin.ModelAdmin):
    search_fields = ('pessoa', 'setor')
    list_filter = ('pessoa', 'setor')
    ordering = ['pessoa']

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Visita, VisitaAdmin)