from django.shortcuts import render, get_object_or_404, redirect
from .forms import TreinadorForm
from .models import Treinador, Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_treinador(request):
    template_name = 'treinadores/add_treinador.html'
    context = {}
    if request.method == 'POST':
        form = TreinadorForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('treinadores:list_treinadores')
    form = TreinadorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_treinadores(request):
    template_name = 'treinadores/list_treinadores.html'
    treinadores = Treinador.objects.filter()
    context = {
        'treinadores': treinadores
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_treinador(request, id_treinador):
    template_name = 'treinadores/add_treinador.html'
    context ={}
    treinador = get_object_or_404(Treinador, id=id_treinador)
    if request.method == 'POST':
        form = TreinadorForm(request.POST, request.FILES,  instance=treinador)
        if form.is_valid():
            form.save()
            return redirect('treinadores:list_treinadores')
    form = TreinadorForm(instance=treinador)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_treinador(request, id_treinador):
    treinador = Treinador.objects.get(id=id_treinador)
    treinador.delete()
    return redirect('treinadores:list_treinadores')

def search_treinadores(request):
    template_name = 'treinadores/list_treinadores.html'
    query = request.GET.get('query')
    categorias = Category.objects.filter()
    treinadores = Treinador.objects.filter(name__icontains=query)
    context = {
        'treinadores': treinadores,
        'categorias': categorias,
    }
    return render(request,template_name, context)