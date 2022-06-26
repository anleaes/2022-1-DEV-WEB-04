from django.urls import path
from . import views

app_name = 'treinadores'

urlpatterns = [
    path('', views.list_treinadores, name='list_treinadores'),
    path('adicionar/', views.add_treinador, name='add_treinador'),
    path('editar/<int:id_treinador>/', views.edit_treinador, name='edit_treinador'),
    path('excluir/<int:id_treinador>/', views.delete_treinador, name='delete_treinador'),
    path('buscar/', views.search_treinadores, name='search_treinadores'),
]
