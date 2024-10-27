from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientesViewSet, FornecedoresViewSet, NumeroSerieViewSet, ProdutosViewSet, GrupoProdutoViewSet, FamiliaProdutoViewSet, MovimentarEstoqueViewSet


router = DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'grupo-produto', GrupoProdutoViewSet)
router.register(r'familia-produto', FamiliaProdutoViewSet)
router.register(r'movimentar-estoque', MovimentarEstoqueViewSet)
router.register(r'numeros-serie', NumeroSerieViewSet, basename='numeros-serie')

urlpatterns = [
    path('', include(router.urls)),
]

