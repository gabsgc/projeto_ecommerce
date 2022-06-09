from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cadastrar_produto, name='cadastrar_produto'),
    path('buscar/<str:nome>', views.buscar_produto, name='produto'),
    path('deletar/<int:id>', views.deletar_produto, name='deletar_produto')
]
