from django.shortcuts import render, get_object_or_404, redirect
from .forms import AcademiaForm
from .models import Academia, Category, Treinador, AcademiaCategory, AcademiaTreinador
from django.contrib.auth.decorators import login_required

@login_required(login_url='/contas/login/')
def add_academia(request):
    template_name = 'academias/add_academia.html'
    context = {}
    if request.method == 'POST':
        form = AcademiaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('academias:list_academias')
    form = AcademiaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_academias(request):
    template_name = 'academias/list_academias.html'
    academia_categories = AcademiaCategory.objects.filter()
    academia_treinadores = AcademiaTreinador.objects.filter()
    categories = Category.objects.filter()
    treinadores = Treinador.objects.filter()
    academias = Academia.objects.filter()
    context = {
        'academias': academias,
        'categories': categories,
        'treinadores': treinadores,
        'academia_categories': academia_categories,
        'academia_treinadores': academia_treinadores
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_academia(request, id_academia):
    template_name = 'academias/add_academia.html'
    context ={}
    academia = get_object_or_404(Academia, id=id_academia)
    if request.method == 'POST':
        form = AcademiaForm(request.POST, instance=academia)
        if form.is_valid():
            form.save()
            return redirect('academias:list_academias')
    form = AcademiaForm(instance=academia)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_academia(request, id_academia):
    academia = Academia.objects.get(id=id_academia)
    academia.delete()
    return redirect('academias:list_academias')