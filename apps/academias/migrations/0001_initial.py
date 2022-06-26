# Generated by Django 3.2.5 on 2022-06-22 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('treinadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Academia',
                'verbose_name_plural': 'Academias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AcademiaTreinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academias.academia')),
                ('treinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinadores.treinador')),
            ],
            options={
                'verbose_name': 'Item de Treinador',
                'verbose_name_plural': 'Itens de Treinador',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AcademiaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academias.academia')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Item de Categoria',
                'verbose_name_plural': 'Itens de Categoria',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='academia',
            name='academia_category',
            field=models.ManyToManyField(blank=True, through='academias.AcademiaCategory', to='categories.Category'),
        ),
        migrations.AddField(
            model_name='academia',
            name='academia_treinador',
            field=models.ManyToManyField(blank=True, through='academias.AcademiaTreinador', to='treinadores.Treinador'),
        ),
    ]
