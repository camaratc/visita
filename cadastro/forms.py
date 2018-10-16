from django import forms
from django.forms import widgets
import simplejson as json

from .models import Pessoa
from .models import Visita

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade')
    
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        self.fields['estado'] = forms.CharField(widget=forms.Select())
        self.fields['cidade'] = forms.CharField(widget=forms.Select())

        # self.fields['estado'].widget = forms.Select(attrs={'class': 'browser-default'})
        # self.fields['cidade'].widget = forms.Select(attrs={'class': 'browser-default'})

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ('pessoa', 'setor', 'observacao')

    def __init__(self, *args, **kwargs):
        super(VisitaForm, self).__init__(*args, **kwargs)

        self.fields['observacao'].required = False
        self.fields['observacao'].widget = forms.Textarea(attrs={'class': 'materialize-textarea'})
