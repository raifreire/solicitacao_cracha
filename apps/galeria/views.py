from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Cracha
from apps.galeria.forms import CrachaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    crachas = Cracha.objects.order_by("data_cracha").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": crachas})

def imagem(request, foto_id):
    crachas = get_object_or_404(Cracha, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"crachas": crachas})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    crachas = Cracha.objects.order_by("data_cracha").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            crachas = crachas.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": crachas})

def novo_cracha(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = CrachaForms
    if request.method == 'POST':
        form = CrachaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cracha criado!')
            return redirect('index')

    return render(request, 'galeria/novo_cracha.html', {'form': form})

def editar_cracha(request, foto_id):
    cracha = Cracha.objects.get(id=foto_id)
    form = CrachaForms(instance=cracha)

    if request.method == 'POST':
        form = CrachaForms(request.POST, request.FILES, instance=cracha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cracha editado com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_cracha.html', {'form': form, 'foto_id': foto_id})

def deletar_cracha(request, foto_id):
    cracha = Cracha.objects.get(id=foto_id)
    cracha.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, status):
    print(status)
    crachas = Cracha.objects.order_by("data_cracha").filter(publicada=True)

    return render(request, 'galeria/index.html', {"cards": crachas})