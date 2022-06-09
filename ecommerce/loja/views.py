from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from loja.models import Produto
from django.template import loader

produtos = Produto.objects.all()

def index(request):
    return render(template_name="index.html", request=request, context={'produto': produtos})

def cadastrar_produto(request):
    if request.method == "GET":
        return render(template_name="cadastro.html", request=request)
    elif request.method == "POST":
        if request.POST.get('ativo') == 'on':
            ativo = True
        else:
            ativo = False
        produto = Produto()
        produto.nome = request.POST.get('nome', None)
        produto.qtd_estoque = request.POST.get('qtd_estoque', None)
        produto.preco_unitario = request.POST.get('preco_unitario', None)
        produto.imagem = request.POST.get('imagem', None)
        produto.ativo = ativo
        produto.save()
        return render(template_name="index.html", request=request, context={'produto': produtos})
    
def buscar_produto(request, nome):
    if request.method == "GET":
        busca = Produto.objects.filter(nome = nome)
        return render(request, "index.html", {"produto": busca})
    return render(request, "index.html", {"produto": produtos,"erro":"Produto não encontrado." })

def deletar_produto(request, id):
    if request.method == "GET":
        produto = Produto.objects.filter(id=id)
        produto.delete()
        return render(request, "index.html", {"produto": produtos})
    return render(request, "index.html", {"produto": produtos})

def editar(request, id):
    produto = Produto.objects.get(id=id)
    template = loader.get_template('editar.html')
    context = {
        'produto': produto,
    }
    return HttpResponse(template.render(context, request))
  
def atualizar_produto(request, id):
    nome = request.POST['nome']
    qtd_estoque = request.POST['qtd_estoque']
    preco_unitario = request.POST['preco_unitario']
    ativo = True
    produto = Produto.objects.get(id=id)
    produto.nome = nome
    produto.qtd_estoque = qtd_estoque
    produto.preco_unitario = preco_unitario
    produto.ativo = ativo
    produto.save()
    return HttpResponseRedirect(reverse('index'))