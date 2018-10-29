from django import forms
from django.forms import widgets

from .models import Pessoa
from .models import Visita

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade', 'foto_principal', 'foto_adicional')
    
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        self.fields['estado'] = forms.CharField(widget=forms.Select())
        self.fields['cidade'] = forms.CharField(widget=forms.Select())

class VisitaForm(forms.ModelForm):
    pessoa = forms.ModelChoiceField(queryset=Pessoa.objects.all(), empty_label='Selecionar Visitante')

    class Meta:
        model = Visita
        fields = ('pessoa', 'setor', 'observacao')

    def __init__(self, *args, **kwargs):
        super(VisitaForm, self).__init__(*args, **kwargs)

        self.fields['observacao'].required = False
        self.fields['observacao'].widget = forms.Textarea(attrs={'class': 'materialize-textarea'})
        self.fields['pessoa'].widget = forms.HiddenInput()

class FiltroHistoricoForm(forms.Form):
    # cod = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control cod'}))
    busca = forms.CharField(required=False)
    data_inicial = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
