from django.contrib import admin
from django.urls import path
from django.templatetags.static import static
from .models import Categoria, ItemPedido, Produto, Lote, Pedido, MovimentacaoProduto, RegistroFinanceiro, Subcategoria
from .forms import ItemPedidoForm  # Importa o formulário personalizado

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Subcategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria__nome']
    search_fields = ['nome']
    
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'subcategoria', 'preco_venda']
    search_fields = ['nome']
    list_filter = ['categoria', 'subcategoria']

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'preco_custo', 'data_entrada']
    search_fields = ['produto__nome']
    list_filter = ['produto__categoria', 'produto__subcategoria']


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    fields = ('produto', 'quantidade')
    form = ItemPedidoForm  # Usa o formulário personalizado

    class Media:
        js = (static('js/pedido_total.js'),)  # Adiciona o JavaScript
        
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'valor_total', 'forma_pagamento', 'data_pedido']
    list_filter = ['forma_pagamento', 'data_pedido']
    inlines = [ItemPedidoInline]  # Adiciona o inline


@admin.register(MovimentacaoProduto)
class MovimentacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ['lote', 'tipo', 'quantidade', 'data_movimentacao']
    list_filter = ['tipo', 'data_movimentacao']
