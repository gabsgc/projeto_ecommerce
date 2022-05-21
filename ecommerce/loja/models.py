from django.db import models

class Pedido(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    valor_total = models.IntegerField()
    ativo = models.BooleanField()

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    qtd_estoque = models.IntegerField()
    preco_unitario = models.FloatField()
    imagem = models.TextField()
    ativo = models.BooleanField()

class PedidoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    desconto = models.DecimalField(decimal_places=2, max_digits=9)
