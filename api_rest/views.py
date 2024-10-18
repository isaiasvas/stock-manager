from rest_framework import viewsets
from .models import Categoria, Lote, Produto, Pedido, MovimentacaoProduto, RegistroFinanceiro, Subcategoria
from .serializers import CategoriaSerializer, LoteSerializer, ProdutoSerializer, PedidoSerializer, RegistroFinanceiroSerializer, MovimentacaoProdutoSerializer, SubcategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubcategoriaViewSet(viewsets.ModelViewSet):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class MovimentacaoProdutoViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoProduto.objects.all()
    serializer_class = MovimentacaoProdutoSerializer


class RegistroFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = RegistroFinanceiro.objects.all()
    serializer_class = RegistroFinanceiroSerializer
