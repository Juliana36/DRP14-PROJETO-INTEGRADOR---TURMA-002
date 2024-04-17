from django import forms
from models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class meta:
        model = OrdemServico
        fields = ['tmo', 'dataservico',  'quantidade', 'custo']
