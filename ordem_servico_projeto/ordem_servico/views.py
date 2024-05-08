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

    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    for ordem in ordens_servico:
        
        data_sem_fuso_horario = ordem.data.replace(tzinfo=None)
        ws.append([ordem.empresa, ordem.servico, ordem.produto, data_sem_fuso_horario])

    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    response['Content-Disposition'] = f'attachment; filename=ordens_servico_{mes}.xlsx'
    
    wb.save(response)

    return response

    return response

def historico_ordem_servico(request, mes=None):
    if mes and 1 <= 12:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
        mes = 1 
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    return render(request, 'ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico, 'mes': mes})
   
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    for ordem in ordens_servico:
        ws.append([ordem.empresa, ordem.servico, ordem.produto, ordem.data])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=ordens_servico_{mes}.xlsx'
    wb.save(response)



def emitir_planilha(request, mes, ano):
    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes, data__year=ano)



   
    planilha = "Planilha de Ordens de Serviço para o mês {} do ano {}\n".format(mes, ano)
    for ordem in ordens_servico:
        planilha += "Empresa: {}, Serviço: {}, Data: {}\n".format(ordem.empresa, ordem.servico, ordem.data)

    
    return HttpResponse(planilha, content_type='text/plain')
    return response



