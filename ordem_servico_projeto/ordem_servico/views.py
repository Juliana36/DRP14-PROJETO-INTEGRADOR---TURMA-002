from django.shortcuts import render
from .forms import OrdemServicoForm
from django.http import HttpResponse
from openpyxl import Workbook
from .models import EmissaoOrdemServico
from django.shortcuts import render, redirect

def criar_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['loja']
            servico = form.cleaned_data['servico']         
            EmissaoOrdemServico.objects.create(empresa=empresa, servico=servico)
            return redirect('ordem_servico_confirmacao') # Redirecione para a página de confirmação
    else:
        form = OrdemServicoForm()
    return render(request, 'ordem_servico/criar_ordem_servico.html', {'form': form})

def ordem_servico_confirmacao(request):
    return render(request, 'ordem_servico/ordem_servico_confirmacao.html')

def historico_ordem_servico(request, mes=None):
    if mes:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
    return render(request, 'ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico})

def baixar_excel(request, mes):
    
    wb = Workbook()
    ws = wb.active 
    ws.append(['Empresa', 'Serviço', 'Produto', 'Data'])
def historico_ordem_servico(request, mes=None):
    if mes and 1 <= 12:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
        mes = 1 # Define um valor padrão para 'mes'
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    return render(request, 'ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico, 'mes': mes})
   
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    for ordem in ordens_servico:
        ws.append([ordem.empresa, ordem.servico, ordem.produto, ordem.data])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=ordens_servico_{mes}.xlsx'
    wb.save(response)



def emitir_planilha(request, mes, ano):
    # Aqui você pode adicionar a lógica para gerar a planilha com base nos parâmetros mes e ano
    # Por exemplo, você pode filtrar os objetos EmissaoOrdemServico com base nesses parâmetros
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes, data__year=ano)



    # Gere a planilha (este é apenas um exemplo, você precisará adaptar de acordo com suas necessidades)
    planilha = "Planilha de Ordens de Serviço para o mês {} do ano {}\n".format(mes, ano)
    for ordem in ordens_servico:
        planilha += "Empresa: {}, Serviço: {}, Data: {}\n".format(ordem.empresa, ordem.servico, ordem.data)

    # Retorne a planilha como uma resposta HTTP
    return HttpResponse(planilha, content_type='text/plain')
    return response



