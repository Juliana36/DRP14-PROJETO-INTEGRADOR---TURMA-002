from django.db import models
from datetime import date
from choices import TMO_CHOICES , DEALER_CHOICES




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
            
                
        #self.Prest = prest

    def setTMO(self, tmo): #Define o TMO
        self.TMO = tmo
    
    def getTMO(self):#Retorna o TMO
        return self.TMO
    
    def setDescServ(self, desc):#Define a descrição
        self.DescServ = desc
    
    def getDescServ(self):#retorna a descrição
        return self.DescServ

    def setCustoUnit(self, custo):#Define o Custo
        self.CustoUnit = custo
    
    def attCustoUnit(self, custo):#Atualiza o Custo
        self.CustoUnit = custo

    def getCustoUnit(self):##retorna o custo
        return self.CustoUnit

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
    
    

    def setNomeLoja (self, nome):
        self.NomeLoja = nome
    
    def getNomeLoja (self):
        return self.NomeLoja

    '''def setEndereço (self, endereço):
        self.Endereço = endereço
    
    def getEndereço(self):
        return self.Endereço'''
    
    def setDealer (self, codigo):
        self.Dealer = codigo

    def getDealer(self):
        return self.Dealer

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