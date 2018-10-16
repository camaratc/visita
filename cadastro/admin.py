from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade', 'dataCadastro')
    list_filter = ('estado', 'cidade', ('dataCadastro', DateTimeRangeFilter))
    list_display = ('nome', 'cpf', 'rg', 'endereco','bairro', 'estado', 'cidade', 'dataCadastro')
    ordering = ['nome']

admin.site.register(Pessoa, PessoaAdmin)