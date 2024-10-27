from django.contrib import admin
from .models import Clientes, Fornecedores, Produtos, GrupoProduto, FamiliaProduto, MovimentarEstoque

admin.site.register(Clientes)
admin.site.register(Fornecedores)
admin.site.register(Produtos)
admin.site.register(GrupoProduto)
admin.site.register(FamiliaProduto)
admin.site.register(MovimentarEstoque)
