from django.db import models
from datetime import date
from choices import TMO_CHOICES , DEALER_CHOICES




class Servico:

    def __init__(self, tmo):
        self.TMO=tmo
        self.DescServ = None
        self.CustoUnit = None
        self.ValorCAOA = None
    
    '''TMO = models.CharField(max_length=50, choices=TMO_CHOICES)
    DescServ = models.CharField(max_length=255)
    CustoUnit = models.FloatField()
    ValorCAOA = models.FloatField()'''
    
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

class OrdemServico:
    
    def __init__(self, numos,data):
        self.NumOs = numos
        self.Data = data
        self.Dealer = None
        self.Quinzena = None
        self.TMOS= []

    '''NumOS = models.IntegerField(primary_key=True, unique=True)#numero da OS
    DataServ = models.DateField()#Data do serviço
    Quinzena = models.IntegerField(choices=((1, '1ª Quinzena'), (2, '2ª Quinzena')))#Quinzena
    Dealer = models.CharField()
    tmo = models.CharField(max_length=50, choices=TMO_CHOICES)#Lista de TMOS'''
    
    def adicionarServ(self,servico):
        self.TMOS.append(servico)

    def setNumOS(self, num):#Define o numero da OS
        self.NumOS = num
    
    def getNumOS(self):#Retorna o numero da OS
        return self.NumOS
    
    def setDataServ(self, data):#Define a data da OS
        self.DataServ = data
    
    def getDataServ(self):#Retorna a data da OS
        return self.DataServ

    def setQuinzenaMes(self):#Define se esta na primeira quinzena ou na segunda quinzena do mes em base no dia que a os for registrada
        data_atual = date.today()
        if data_atual.day <= 15:
            self.Quinzena = 1
        else:
            self.Quinzena = 2

    def getQuinzenaMes(self):#Retorna a quinzena
        return self.quinzena

    def setDealer(self, Dealer):
        self.Dealer = Dealer
    
    def getDealer(self):
        return self.Dealer
    
    def __str__(self):
        return f"OS-{self.NumOs} ({self.TMOS})"
    
    

    
  
   
