from django.db import models
from datetime import date
from .choices import TMO_CHOICES , DEALER_CHOICES




class Servico:

    def __init__(self, tmo):
        self.TMO=tmo
        self.DescServ = None
        self.CustoUnit = None
        self.ValorCAOA = None
    
    
    def buscar_dados(self):
        for codigo_tabela, descricao, custo, valor in TMO_CHOICES:
            if self.TMO == codigo_tabela:
                self.DescServ = descricao
                self.CustoUnit = custo
                self.ValorCAOA = valor
                break

    def __str__(self):
        return self.DescServ

    def printServ(self):
        print(self.TMO, self.DescServ, self.CustoUnit, self.ValorCAOA)

class Loja:

    def __init__ (self, dealer):
        self.DEALER = dealer
        self.NomeLoja = None
    
    def buscar_dados(self):#
        for codigo_tabela, nome_loja in DEALER_CHOICES:
            if self.DEALER == codigo_tabela:
                self.NomeLoja = nome_loja
                break
    
    

    def __str__(self):
        return self.NomeLoja


class OrdemDeServico(models.Model):
    numero_os = models.CharField(max_length=50)
    data_servico = models.DateField()
    descricao_pedido = models.TextField()
    tmos_selecionados = models.JSONField()

    def adicionar_tmo(self, tmo):
        # Aqui você pode chamar a função da classe Servico para buscar os dados do TMO e adicionar à ordem de serviço
        servico = Servico.buscar_dados(tmo)
        # Lógica para adicionar o TMO à ordem de serviço
        self.tmos.add(servico)


    
    def __str__(self):
        return f"OS-{self.numero_os} ({self.TMOS})"


