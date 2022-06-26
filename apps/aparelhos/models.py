from django.db import models
from categories.models import Category

# Create your models here.
class Aparelho(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    photo = models.ImageField('Foto', upload_to='photos')
    aparelho_category = models.ManyToManyField(Category, through='AparelhoCategory', blank=True)
    
    class Meta:
        verbose_name = 'Aparelho'
        verbose_name_plural = 'Aparelhos'
        ordering =['id']

class AparelhoCategory(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    aparelho = models.ForeignKey(Aparelho, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria do Aparelho'
        verbose_name_plural = 'Categoria do Aparelho'
        ordering =['id']

    def __str__(self):
        return self.category.name


    def __str__(self):
        return self.name