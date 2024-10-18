from django.forms import ValidationError
from rest_framework import serializers
from .models import Produto, Categoria, Subcategoria, ItemPedido, Pedido, Lote, MovimentacaoProduto, RegistroFinanceiro

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())  # Usa ID do produto

    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)  # Inclui os itens do pedido

    class Meta:
        model = Pedido
        fields = ['numero', 'valor_total', 'forma_pagamento', 'troco', 'data_pedido', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)

        # Criar cada ItemPedido associado ao Pedido
        for item_data in itens_data:
            ItemPedido.objects.create(
                pedido=pedido,
                produto_id=item_data['produto'].id,  # Acessando o ID do produto diretamente
                quantidade=item_data['quantidade']
            )

        try:
            pedido.realizar_saida_estoque()  # Realiza a saída de estoque após criar o pedido
        except ValidationError as e:
            pedido.delete()  # Desfaz a criação do pedido
            raise serializers.ValidationError(str(e))

        return pedido

class LoteSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())  # Espera receber apenas o ID do produto

    class Meta:
        model = Lote
        fields = ['id', 'produto', 'quantidade', 'preco_custo', 'data_entrada']

    def create(self, validated_data):
        # Cria o lote normalmente
        lote = Lote.objects.create(**validated_data)

        # Registra uma movimentação de entrada para a quantidade do lote criado
        MovimentacaoProduto.objects.create(
            lote=lote,
            tipo='entrada',
            quantidade=lote.quantidade  # A quantidade deve ser a mesma que foi passada para o lote
        )

        return lote


class MovimentacaoProdutoSerializer(serializers.ModelSerializer):
    lote = LoteSerializer()  # Usar o serializer de lote para incluir detalhes do lote

    class Meta:
        model = MovimentacaoProduto
        fields = ['id', 'tipo', 'quantidade', 'data_movimentacao', 'lote']  # Inclua o lote

class RegistroFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFinanceiro
        fields = '__all__'
