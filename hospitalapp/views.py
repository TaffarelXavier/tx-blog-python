from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform
from .models import Hospital
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def index(request):
    posts = Hospital.objects.all()
    busca = request.GET.get('search')
    if busca:
        posts = Hospital.objects.filter(nome_hospital__icontains=busca)
    return render(request, 'hospitais/index.html', {'hospitais': posts})


def posts(request):
    posts = Hospital.objects.all()
    busca = request.GET.get('search')
    if busca:
        Hospital.objects.filter(nome_hospital__icontains=busca)
    return render(request, "hospitais/jornal.html", {'hospitais': posts})


def criar_post(request):
    form = Hospitalform(request.POST)
    if request.method == "POST":
        form = Hospitalform(request.POST, request.FILES)
    if form.is_valid():
        hosp = form.save()
        hosp.save()
        messages.success(request, 'Post criado com sucesso.')
        form = Hospitalform()

    return render(request, 'hospitais/criar_post.html', {'form': form})


def editar_post(request, id):
    post = get_object_or_404(Hospital, pk=id)
    form = Hospitalform(instance=post)
    if (request.method == 'POST'):
        form = Hospitalform(request.POST, request.FILES, instance=post)
        if (form.is_valid()):
            form.save()
            return redirect('/index/')
        else:
            return render(request, "hospitais/editar_post.html", {'form': form, 'post': post})
    else:
        return render(request, "hospitais/editar_post.html", {'form': form, 'post': post})

def deletar_post(request, id):
    post = get_object_or_404(Hospital, pk=id)
    if request.method == "POST":
        post.delete()
        return redirect('/index/')
    return render(request, 'hospitais/deletar_post.html', {'post': post})
