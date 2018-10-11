from django import forms

from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade')
    
    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        
        # self.fields['host'].required = False

        """ for item in self.fields:
            if item == 'descricao':
                self.fields[item].widget = forms.Textarea(attrs={'class': 'form-control input-descricao'})
            elif item == 'email':
                self.fields[item].widget = forms.EmailInput(attrs={'class': 'form-control'})
            else:
                self.fields[item].widget = forms.TextInput(attrs={'class': 'form-control'}) """