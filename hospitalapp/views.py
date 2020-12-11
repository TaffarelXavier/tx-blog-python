from django.shortcuts import render
# from django.http import HttpResponse
from .forms import PostsForm, Hospitalform
from .models import Post, TelaInicial
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def index(request):
    tela_inicial = TelaInicial.objects.all()
    posts = Post.objects.all()
    busca = request.GET.get('search')
    if busca:
        posts = Post.objects.filter(titulo__icontains=busca)
    return render(request, 'hospitais/index.html', {'posts': posts, 'telainicial': tela_inicial})


# def posts(request):
#     posts = Post.objects.all()
#     busca = request.GET.get('search')
#     if busca:
#         posts = Post.objects.filter(titulo__icontains=busca)
#     return render(request, "hospitais/jornal.html", {'hospitais': posts})


def criar_post(request):
    form = PostsForm(request.POST)
    posts = Post.objects.all()
    tela_inicial = TelaInicial.objects.all()
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save()
        post.save()
        messages.success(request, 'Post criado com sucesso.')
        form = PostsForm()

    return render(request, 'posts/criar_post.html', {'form': form, 'posts': posts, 'telainicial': tela_inicial})


def editar_post(request, id):
    post = get_object_or_404(Post, pk=id)
    form = Hospitalform(instance=post)
    if (request.method == 'POST'):
        form = Hospitalform(request.POST, request.FILES, instance=post)
        if (form.is_valid()):
            form.save()
            return redirect('index')
        else:
            return render(request, "posts/editar_post.html", {'form': form, 'post': post})
    else:
        return render(request, "posts/editar_post.html", {'form': form, 'post': post})


def deletar_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.delete()
        return redirect('index')
    return render(request, 'posts/deletar_post.html', {'post': post})
