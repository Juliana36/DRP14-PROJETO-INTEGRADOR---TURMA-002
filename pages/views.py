from django.shortcuts import render
from django.views.generic import TemplateView
from .models import OrdemDeServico
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'home.html'
def home(request):
    return render(request, 'home.html')
def servicos(request):
    return render(request, 'servicos.html')


def ordem_de_servico(request):
    return render(request, 'ordem_de_servico.html')

def processar_servico(request):
    if request.method == 'POST':
        numero_os = request.POST.get('numero_os')
        data_servico = request.POST.get('data_servico')
        descricao_pedido = request.POST.get('descricao_pedido')
        tmos_selecionados = request.POST.getlist('tmo_servico')

        # Criar uma nova ordem de serviço
        ordem = OrdemDeServico(numero_os=numero_os, data_servico=data_servico, descricao_pedido=descricao_pedido)
        ordem.save()

        # Adicionar os TMOs selecionados à ordem de serviço
        for tmo in tmos_selecionados:
            ordem.adicionar_tmo(tmo)

        return HttpResponse(json.dumps({'message': 'Ordem de Serviço recebida com sucesso!'}), content_type="application/json")

    return HttpResponse(status=405)  # Método não permitido
