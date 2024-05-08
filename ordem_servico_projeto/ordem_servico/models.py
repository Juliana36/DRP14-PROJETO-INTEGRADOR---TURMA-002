from django.db import models

class Loja(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    preco_min = models.DecimalField(max_digits=10, decimal_places=2)
    preco_max = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo


class EmissaoOrdemServico(models.Model):
    empresa = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True) 

    
    def __str__(self):
        return self.nome
    

