from django.db import models

# Create your models here.

class Clientes(models.Model):
    # Definindo constantes para os tipos de cliente
    FISICA = 'fisica'
    JURIDICA = 'juridica'

    # Definindo constantes para sexo
    MASCULINO = 'masculino'
    FEMININO = 'feminino'
    NAO_INFORMAR = 'nao_informar'

    # Usando uma tupla para as opções de tipo de cliente
    TIPO_CLIENTE_CHOICES = [
        (FISICA, "Fisica"),
        (JURIDICA, "Juridica"),
    ]

    # Usando uma tupla para as opções de sexo
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
        (NAO_INFORMAR, 'Não informar'),
    ]

    # Campos da tabela
    tipo_cliente = models.CharField(
        max_length= 10,
        choices=TIPO_CLIENTE_CHOICES,
        default=FISICA,
    )
    nome = models.CharField(max_length=100)
    pessoa_contato = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(
        max_length=15,
        choices=SEXO_CHOICES,
        default=NAO_INFORMAR
    )
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    codigo_bacen = models.CharField(max_length=20, blank=True, null=True)
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True)
    ie_rg = models.CharField(max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField(max_length=20, blank=True, null=True)
    suframa = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='clientes_fotos/', blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Fornecedores(models.Model):
    nome_fornecedor = models.CharField(max_length=100)
    pessoa_contato = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    codigo_bacen = models.CharField(max_length=20, blank=True, null=True)
    cnpj_cpf = models.CharField(max_length=14, blank=True, null=True)
    ie_rg = models.CharField(max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome_fornecedor
    
class GrupoProduto(models.Model):
    nome_grupo = models.CharField(max_length=100)
    sub_grupo_nivel_1 = models.CharField(max_length=100, blank=True, null=True)
    sub_grupo_nivel_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_grupo    
    
class FamiliaProduto(models.Model):
    nome_familia = models.CharField(max_length=100)
    sub_familia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome_familia

class Produtos(models.Model):
    cod_produto = models.CharField(max_length=50, unique=True)
    cod_barras = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=200)
    estoque = models.PositiveIntegerField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    custo_medio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lucro_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.DecimalField(max_digits=10, decimal_places=2)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.SET_NULL, null=True, related_name="produtos")
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.SET_NULL, null=True, related_name="produtos")
    familia = models.ForeignKey(FamiliaProduto, on_delete=models.SET_NULL, null=True, related_name="produtos")
    foto = models.ImageField(upload_to='produtos_fotos/', blank=True, null=True)

    def __str__(self):
        return self.descricao
    
    
class MovimentarEstoque(models.Model):
    TIPO_MOVIMENTACAO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(max_length=10, choices=TIPO_MOVIMENTACAO_CHOICES)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    quantidade = models.PositiveIntegerField()
    descricao_movimentacao = models.TextField()

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.produto.descricao} ({self.quantidade})"
    
class NumeroSerie(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name="numeros_serie")
    numero_serie = models.CharField(max_length=100)
    nf_compra = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Produto: {self.produto.descricao}, Série: {self.numero_serie}"
    
    