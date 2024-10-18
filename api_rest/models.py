from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome} - {self.subcategoria.nome}'

class Lote(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Relacionamento com Produto
    quantidade = models.IntegerField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Lote de {self.produto.nome} - {self.data_entrada}'


class MovimentacaoProduto(models.Model):
    TIPO_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    ]
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_MOVIMENTACAO)
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Remover a lógica de subtração de quantidade ao salvar movimentação
        if self.tipo == 'saida':
            # Não alterar a quantidade do lote aqui
            if self.lote.quantidade < self.quantidade:
                raise ValidationError("Quantidade insuficiente no lote.")
        
        super().save(*args, **kwargs)  # Salva a movimentação sem alterar a quantidade do lote


class Pedido(models.Model):
    numero = models.AutoField(primary_key=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)
    troco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def realizar_saida_estoque(self):
        # Utiliza uma transação para garantir que não haja modificações parciais
        with transaction.atomic():
            for item in self.itens.all():
                quantidade_desejada = item.quantidade  # Quantidade a ser subtraída no total
                lotes = Lote.objects.filter(produto=item.produto).order_by('data_entrada')

                for lote in lotes:
                    if quantidade_desejada <= 0:
                        break  # Se já subtraiu tudo, encerra

                    if lote.quantidade > 0:
                        quantidade_a_subtrair = min(lote.quantidade, quantidade_desejada)
                        # Atualiza a quantidade do lote de forma segura
                        self.registrar_movimentacao(lote, quantidade_a_subtrair, 'saida')
                        lote.quantidade -= quantidade_a_subtrair
                        quantidade_desejada -= quantidade_a_subtrair
                        lote.save()  # Salva o estado atualizado do lote

                # Se ainda há quantidade a ser subtraída após tentar todos os lotes, lança erro
                if quantidade_desejada > 0:
                    raise ValidationError(f"Estoque insuficiente para o produto: {item.produto.nome}")

    def registrar_movimentacao(self, lote, quantidade, tipo):
        MovimentacaoProduto.objects.create(
            lote=lote,
            tipo=tipo,
            quantidade=quantidade
        )

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

class RegistroFinanceiro(models.Model):
    TIPO_REGISTRO = [
        ('gasto', 'Gasto'),
        ('recebido', 'Recebido')
    ]
    tipo = models.CharField(max_length=8, choices=TIPO_REGISTRO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
