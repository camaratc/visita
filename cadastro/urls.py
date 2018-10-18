from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.cadastro_pessoas, name='cadastro_pessoas'),
    path('visitas/', views.cadastro_visitas, name='cadastro_visitas'),
    path('historico/', views.historico_visitas, name='historico_visitas'),
    path('visita/<int:pk>', views.visita_detalhes, name='visita_detalhes'),
    path('visita/<int:pk>#', views.confirmar_saida, name='confirmar_saida'),
]