from django.db import models
from .choices import TMO_CHOICES, DEALER_CHOICES

class Servico(models.Model):
    TMO = models.CharField(max_length=50, choices=TMO_CHOICES)
    DescServ = models.CharField(max_length=255)
    CustoUnit = models.DecimalField(max_digits=10, decimal_places=2)
    ValorCAOA = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.DescServ

class Loja(models.Model):
    DEALER = models.CharField(max_length=50, choices=DEALER_CHOICES)
    NomeLoja = models.CharField(max_length=255)

    def __str__(self):
        return self.NomeLoja

class OrdemDeServico(models.Model):
    numero_os = models.CharField(max_length=50)
    data_servico = models.DateField()
    descricao_pedido = models.TextField()
    tmos_selecionados = models.JSONField()

    def __str__(self):
        return f"OS-{self.numero_os}"
