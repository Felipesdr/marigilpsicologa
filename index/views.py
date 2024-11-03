from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from index.models import Texto


def index(request):
    artigos = Texto.objects.filter(visivel=True).order_by('-id')[:6]
    return render(request, 'index/index.html', {'artigos': artigos})

def textos(request):
    artigos_todos = Texto.objects.filter(visivel=True).order_by('-id')
    for artigo in artigos_todos:
        artigo.conteudo = f'{artigo.conteudo[:250]}...'
    paginator = Paginator(artigos_todos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'textos/textos.html', {'page_obj': page_obj})


def texto(request, artigo_id):
    texto = get_object_or_404(Texto, pk=artigo_id)
    return render(request, 'textos/texto.html', {"texto": texto})

def buscar(request):
    textos = Texto.objects.all()
    if "buscar" in  request.GET:
        palavra_buscada = request.GET["buscar"]
        if palavra_buscada:
            textos_filtrados = [texto for texto in textos if palavra_buscada in texto.titulo]
            for texto in textos_filtrados:
                texto.conteudo = f'{texto.conteudo[:250]}...'
    paginator = Paginator(textos_filtrados, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "textos/buscar.html", {"textos_filtrados": page_obj})
