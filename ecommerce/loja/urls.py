from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.listar_produtos, name='produtos'),
    path('cadastrar', views.cadastrar_produto, name='cadastrar_produto'),
    path('buscar/<str:nome>', views.buscar_produto, name='buscar_produto'),
    path('deletar/<id>', views.deletar_produto, name='deletar_produto'),
    path('atualizar/<int:id>', views.editar, name='atualizar'),
    path('atualizar/atualizar-produto/<int:id>', views.atualizar_produto, name='atualizar_produto')
]
