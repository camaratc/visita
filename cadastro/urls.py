from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.cadastro_pessoas, name='cadastro_pessoas'),
    path('visitas/', views.cadastro_visitas, name='cadastro_visitas'),
    path('estados/', views.get_estados, name='estados'),
    path('cidades/', views.get_cidades, name='cidades')
]