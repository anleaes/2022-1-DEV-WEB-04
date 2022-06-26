from django.urls import path
from . import views

app_name = 'aparelhos'

urlpatterns = [
    path('', views.list_aparelhos, name='list_aparelhos'),
    path('adicionar/', views.add_aparelho, name='add_aparelho'),
    path('editar/<int:id_aparelho>/', views.edit_aparelho, name='edit_aparelho'),
    path('excluir/<int:id_aparelho>/', views.delete_aparelho, name='delete_aparelho'),
]