from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AparelhoForm
from .models import Aparelho, Category, AparelhoCategory

# Create your views here.
@login_required(login_url='/contas/login/')
def add_aparelho(request):
    template_name = 'aparelhos/add_aparelho.html'
    context = {}
    if request.method == 'POST':
        form = AparelhoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('aparelhos:list_aparelhos')
    form = AparelhoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_aparelhos(request):
    template_name = 'aparelhos/list_aparelhos.html'
    aparelho_categories = AparelhoCategory.objects.filter()
    categories = Category.objects.filter()
    aparelhos = Aparelho.objects.filter()
    context = {
        'aparelhos': aparelhos,
        'categories': categories,
        'aparelho_categories': aparelho_categories
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_aparelho(request, id_aparelho):
    template_name = 'aparelhos/add_aparelho.html'
    context ={}
    aparelho = get_object_or_404(Aparelho, id=id_aparelho)
    if request.method == 'POST':
        form = AparelhoForm(request.POST, request.FILES,  instance=aparelho)
        if form.is_valid():
            form.save()
            return redirect('aparelhos:list_aparelhos')
    form = AparelhoForm(instance=aparelho)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_aparelho(request, id_aparelho):
    aparelho = Aparelho.objects.get(id=id_aparelho)
    aparelho.delete()
    return redirect('aparelhos:list_aparelhos')