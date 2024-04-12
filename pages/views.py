from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
def home(request):
    return render(request, 'home.html')
def servicos(request):
    return render(request, 'servicos.html')
def ordem_de_servico(request):
    return render(request, 'ordem_de_servico.html')
