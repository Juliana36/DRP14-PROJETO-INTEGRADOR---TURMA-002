from django.test import TestCase
from models import Servico, OrdemServico, Loja

Ser1 = Servico('STLAVCRISTAL')
Ser1.buscar_dados()
Ser1.printServ()
print('')
OrdServ = OrdemServico('001', '20/02/2024')
OrdServ.setQuinzenaMes()
loja01 = Loja('0110FO')
loja01.buscar_dados()
OrdServ.setDealer(loja01)
OrdServ.adicionarServ(Ser1)
print(OrdServ.__str__())
