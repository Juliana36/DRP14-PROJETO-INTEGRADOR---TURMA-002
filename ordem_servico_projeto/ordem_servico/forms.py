from django import forms
from .models import Loja, Servico

class OrdemServicoForm(forms.Form):
    loja = forms.ModelChoiceField(queryset=Loja.objects.all())
    servico = forms.ModelChoiceField(queryset=Servico.objects.all())
    

def salvar_ordem_servico(request, form):
    servico = form.cleaned_data['servicos']
