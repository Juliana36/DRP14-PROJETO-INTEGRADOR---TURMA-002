from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from ordem_servico import views as ordem_servico_views  # Importa as views do aplicativo ordem_servico
from ordem_servico import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='criar_ordem_servico'), name='index'),
    path('criar_ordem_servico/', ordem_servico_views.criar_ordem_servico, name='criar_ordem_servico'),
    path('admin/', admin.site.urls),  # Adiciona as URLs do painel de administração
    path('ordem_servico_confirmacao/', views.ordem_servico_confirmacao, name='ordem_servico_confirmacao'),
    path('emitir_planilha/<int:mes>/<int:ano>/', views.emitir_planilha, name='emitir_planilha'),
    path('historico_ordem_servico/', views.historico_ordem_servico, name='historico_ordem_servico'),
    # Adicione outras URLs conforme necessário
]
