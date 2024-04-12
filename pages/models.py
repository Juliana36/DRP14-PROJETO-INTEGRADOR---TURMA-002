from django.db import models
from datetime import date


class Servico:
    def __init__(self, tmo, desc_serv, custo_unit, prest):
        self.TMO = tmo
        self.DescServ = desc_serv
        self.CustoUnit = custo_unit
        self.Prest = prest

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

    def setPrest(self, prestador):#Define o Prestador de serviço
        self.Prest = prestador
    
    def getPrest(self):
        return self.Prest

    def print (self):
        print(self.TMO, self.DescServ)

class Loja:
    def __init__(self, nomeLoja, endereço, Dealer):
        self.NomeLoja = nomeLoja
        self.Endereço = endereço
        self.Dealer = Dealer

    def setNomeLoja (self, nome):
        self.NomeLoja = nome
    
    def getNomeLoja (self):
        return self.NomeLoja

    def setEndereço (self, endereço):
        self.Endereço = endereço
    
    def getEndereço(self):
        return self.Endereço
    
    def setDealer (self, codigo):
        self.Dealer = codigo

    def getDealer(self):
        return self.Dealer

class OrdemServico(Servico):
    NumOS = models.IntegerField(primary_key=True, unique=True)#numero da OS
    DataServ = models.DateField()#Data do serviço
    Quinzena = models.IntegerField(choices=((1, '1ª Quinzena'), (2, '2ª Quinzena')))#Quinzena


    def setNumOS(self, num):#Define o numero da OS
        self.NumOS = num
    
    def getNumOS(self):#Retorna o numero da OS
        return self.NumOS
    
    def setDataServ(self, data):#Define a data da OS
        self.DataServ = data
    
    def getDataServ(self):#Retorna a data da OS
        return self.DataServ

    def setQuinzenaMes(self, quinzena):#Define se esta na primeira quinzena ou na segunda quinzena do mes em base no dia que a os for registrada
        data_atual = date.today()
        if data_atual.day <= 15:
            self.Quinzena = 1
        else:
            self.Quinzena = 2

    def getQuinzenaMes(self):#Retorna a quinzena
        return self.quinzena
    

    
  
   
