from django.db import models
from django.utils import timezone

import time

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=15)
    rg = models.CharField('RG', max_length=15)
    foto_principal = models.ImageField('Foto do Visitante', upload_to='cadastro/static/img/upload/visitantes/principal/{}'.format(time.strftime("%Y/%m/%d")), blank=True, default='cadastro/static/img/user.svg')
    foto_adicional = models.ImageField('Foto Adicional', upload_to='cadastro/static/img/upload/visitantes/adicional/{}'.format(time.strftime("%Y/%m/%d")), blank=True)
    endereco = models.CharField('Endereço', max_length=255) 
    bairro = models.CharField('Bairro', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    cidade = models.CharField('Cidade', max_length=100)
    dataCadastro = models.DateTimeField('Data de Cadastro', default=timezone.now())

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Visita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField('Data', default=timezone.now())
    horarioEntrada = models.TimeField('Horário de Entrada')
    horarioSaida = models.TimeField('Horário de Saída', null=True, blank=True)
    setor = models.CharField('Setor da Visita', max_length=100)
    observacao = models.TextField('Observação', max_length=1000, blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.pessoa.nome