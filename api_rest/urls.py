from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, LoteViewSet, ProdutoViewSet, PedidoViewSet, MovimentacaoProdutoViewSet, RegistroFinanceiroViewSet, SubcategoriaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet) # Registrando a rota para Produtos
router.register(r'pedidos', PedidoViewSet) # Registrando a rota para Pedidos
router.register(r'movimentacoes', MovimentacaoProdutoViewSet) # Registrando a rota pra movimentacao
router.register(r'financeiro', RegistroFinanceiroViewSet) # Registrando a rota para registro financeiro
router.register(r'categorias', CategoriaViewSet)        # Registrando a rota para categoria
router.register(r'subcategorias', SubcategoriaViewSet)  # Registrando a rota para sub-categoria
router.register(r'lotes', LoteViewSet)  # Registrando a rota para lotes

urlpatterns = [
    path('', include(router.urls)),
]