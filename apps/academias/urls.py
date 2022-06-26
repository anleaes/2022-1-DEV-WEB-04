
from django.urls import path
from . import views

app_name = 'academias'

urlpatterns = [
    path('', views.list_academias, name='list_academias'),
    path('adicionar/', views.add_academia, name='add_academia'),
    path('editar/<int:id_academia>/', views.edit_academia, name='edit_academia'),
    path('excluir/<int:id_academia>/', views.delete_academia, name='delete_academia'),
]