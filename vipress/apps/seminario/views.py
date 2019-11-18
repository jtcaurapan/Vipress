from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from apps.seminario.forms import SeminarioForm
from apps.seminario.models import Seminario


def index_seminario(request):
    if request.method == 'POST':
        form = SeminarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index:index')
    else:
        form = SeminarioForm()

    return render(request, 'seminario/seminario.html', {'form': form})

def seminario_list(request):
    seminario = Seminario.objects.all().order_by('id')
    contexto = {'seminarios':seminario}
    return render(request, 'seminario/seminario_list.html', contexto)

def seminario_edit(request, id_seminario):
    seminario = Seminario.objects.get(id=id_seminario)
    if request.method == 'GET':
        form = SeminarioForm(instance=seminario)
    else:
        form = SeminarioForm(request.POST, instance=seminario)
        if form.is_valid():
            form.save()
        return redirect('seminario:seminario_listar')
    return render(request, 'seminario/seminario.html', {'form':form})

def seminario_delete(request, id_seminario):
    seminario = Seminario.objects.get(id=id_seminario)
    if request.method == 'POST':
        seminario.delete()
        return redirect('seminario:seminario_listar')
    return render(request, 'seminario/seminario_delete.html', {'seminario':seminario})


def index(request):
    return render(request, 'index/index.html')
