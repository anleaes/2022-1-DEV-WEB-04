from django.db import models
from categories.models import Category
from treinadores.models import Treinador

# Create your models here.
class Academia(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereco', max_length=200)   
    cidade = models.CharField('Cidade', max_length=200)
    academia_category = models.ManyToManyField(Category, through='AcademiaCategory', blank=True)
    academia_treinador = models.ManyToManyField(Treinador, through='AcademiaTreinador', blank=True)

    class Meta:
        verbose_name = 'Academia'
        verbose_name_plural = 'Academias'
        ordering =['id']

    def __str__(self):
        return self.name


class AcademiaCategory(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Categoria'
        verbose_name_plural = 'Itens de Categoria'
        ordering =['id']

    def __str__(self):
        return self.category.name

class AcademiaTreinador(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Treinador'
        verbose_name_plural = 'Itens de Treinador'
        ordering =['id']

    def __str__(self):
        return self.treinador.name