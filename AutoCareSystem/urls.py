"""
URL configuration for AutoCareSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('servicos/', views.servicos, name='servicos'),
    path('ordem_de_servico/', views.ordem_de_servico, name='ordem_de_servico'),
    path('servicos/ordem_de_servico/', views.ordem_de_servico, name='ordem_de_servico'),
    path('processar_servico/', views.processar_servico, name='processar_servico'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)