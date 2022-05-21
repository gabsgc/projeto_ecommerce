from django.shortcuts import render
from loja.models import Produto

produtos = Produto.objects.all()

def index(request):
    return render(template_name="index.html", request=request, context={'produto': produtos})
