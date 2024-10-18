from django import forms
from .models import ItemPedido, Produto, Pedido

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona opções de produtos ao campo de seleção
        self.fields['produto'].widget.choices = [
            (produto.id, f"{produto.nome} - R$ {produto.preco_venda}") for produto in Produto.objects.all()
        ]

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido  # Substitua pelo nome correto do seu modelo Pedido
        fields = ['valor_total']  # Inclua outros campos que você precisa

    def save(self, commit=True):
        pedido = super().save(commit=commit)
        pedido.processar_pedido()  # Chama o método para atualizar o estoque
        return pedido
