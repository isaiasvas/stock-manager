from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Clientes, Fornecedores, NumeroSerie, Produtos, GrupoProduto, FamiliaProduto, MovimentarEstoque
from .serializers import (
    ClientesSerializer,
    FornecedoresSerializer,
    NumeroSerieSerializer,
    ProdutosSerializer,
    GrupoProdutoSerializer,
    FamiliaProdutoSerializer,
    MovimentarEstoqueSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Cliente criado com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            cliente = self.get_object()
            serializer = self.get_serializer(cliente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Cliente atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            cliente = self.get_object()
            cliente.delete()
            return Response({"message": "Cliente excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FornecedoresViewSet(viewsets.ModelViewSet):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Fornecedor criado com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            fornecedor = self.get_object()
            serializer = self.get_serializer(fornecedor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Fornecedor atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            fornecedor = self.get_object()
            fornecedor.delete()
            return Response({"message": "Fornecedor excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*10))  # 10 minutos
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Produto criado com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            produto = self.get_object()
            serializer = self.get_serializer(produto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Produto atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            produto = self.get_object()
            produto.delete()
            return Response({"message": "Produto excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GrupoProdutoViewSet(viewsets.ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Grupo de produto criado com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            grupo = self.get_object()
            serializer = self.get_serializer(grupo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Grupo de produto atualizado com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            grupo = self.get_object()
            grupo.delete()
            return Response({"message": "Grupo de produto excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FamiliaProdutoViewSet(viewsets.ModelViewSet):
    queryset = FamiliaProduto.objects.all()
    serializer_class = FamiliaProdutoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Família de produto criada com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            familia = self.get_object()
            serializer = self.get_serializer(familia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Família de produto atualizada com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            familia = self.get_object()
            familia.delete()
            return Response({"message": "Família de produto excluída com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MovimentarEstoqueViewSet(viewsets.ModelViewSet):
    queryset = MovimentarEstoque.objects.all()
    serializer_class = MovimentarEstoqueSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*15))  # 15 minutos
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "Movimentação de estoque criada com sucesso!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            movimentacao = self.get_object()
            serializer = self.get_serializer(movimentacao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Movimentação de estoque atualizada com sucesso!", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            movimentacao = self.get_object()
            movimentacao.delete()
            return Response({"message": "Movimentação de estoque excluída com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NumeroSerieViewSet(viewsets.ModelViewSet):
    queryset = NumeroSerie.objects.all()
    serializer_class = NumeroSerieSerializer
    permission_classes = [IsAuthenticated]