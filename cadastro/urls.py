from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/visitante/', views.cadastro_pessoas, name='cadastro_pessoas'),
    path('cadastrar/visita/', views.cadastro_visitas, name='cadastro_visitas'),
    path('visitante/lista/', views.listar_pessoas, name='listar_pessoas'),
    path('visitante/<int:pk>', views.perfil_pessoa, name='perfil_pessoa'),
    path('visitante/editar/<int:pk>', views.editar_pessoa, name='editar_pessoa'),
    path('visitas/<int:pk>', views.confirmar_saida, name='confirmar_saida'),
    path('visita/<int:pk>', views.visita_detalhes, name='visita_detalhes'),
    path('historico/', views.historico_visitas, name='historico_visitas'),
    path('api/pessoas/', views.api_pessoas, name='api_pessoas'),
]