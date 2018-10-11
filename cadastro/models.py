from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=15)
    rg = models.CharField('RG', max_length=15)
    endereco = models.CharField('Endereço', max_length=255) 
    bairro = models.CharField('Bairro', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    cidade = models.CharField('Cidade', max_length=100)
    dataCadastro = models.DateTimeField('Data de Cadastro', default=timezone.now())

    def __str__(self):
        return self.nome
