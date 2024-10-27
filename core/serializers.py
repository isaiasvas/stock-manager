from rest_framework import serializers
from .models import Clientes, Fornecedores, NumeroSerie, Produtos, GrupoProduto, FamiliaProduto, MovimentarEstoque
from .validators import validar_cnpj, validar_cpf, validar_codigo_bacen

class ClientesSerializer(serializers.ModelSerializer):
    cnpj_cpf = serializers.CharField(validators=[validar_cnpj, validar_cpf], required=False)
    codigo_bacen = serializers.CharField(validators=[validar_codigo_bacen], required=False)

    tipo_cliente = serializers.ChoiceField(
        choices=[('FISICA', 'Física'), ('JURIDICA', 'Jurídica')],
        help_text="Tipo de cliente: 'Física' ou 'Jurídica'."
    )
    nome = serializers.CharField(
        max_length=100,
        help_text="Nome completo do cliente. Exemplo: 'João da Silva'"
    )
    pessoa_contato = serializers.CharField(
        max_length=100,
        required=False,
        help_text="Pessoa para contato no cliente. Exemplo: 'Maria Souza'"
    )
    sexo = serializers.ChoiceField(
        choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('nao_informar', 'Não Informar')],
        help_text="Sexo do cliente: 'Masculino', 'Feminino' ou 'Não Informar'."
    )
    cnpj_cpf = serializers.CharField(
        help_text="CPF ou CNPJ do cliente. Formato esperado: '000.000.000-00' para CPF e '00.000.000/0000-00' para CNPJ."
    )
    telefone = serializers.CharField(
        required=False,
        help_text="Número de telefone. Exemplo: '(11) 1234-5678'"
    )
    celular = serializers.CharField(
        required=False,
        help_text="Número de celular. Exemplo: '(11) 91234-5678'"
    )
    email = serializers.EmailField(
        required=False,
        help_text="Email de contato do cliente. Exemplo: 'cliente@example.com'"
    )


    class Meta:
        model = Clientes
        fields = '__all__'

class FornecedoresSerializer(serializers.ModelSerializer):
    cnpj_cpf = serializers.CharField(validators=[validar_cnpj, validar_cpf], required=False)
    codigo_bacen = serializers.CharField(validators=[validar_codigo_bacen], required=False)

    nome_fornecedor = serializers.CharField(
        max_length=255,
        help_text="Nome do fornecedor. Exemplo: 'Fornecedor ABC'"
    )
    pessoa_contato = serializers.CharField(
        max_length=100,
        required=False,
        help_text="Pessoa para contato no fornecedor. Exemplo: 'Carlos Almeida'"
    )
    cnpj_cpf = serializers.CharField(
        help_text="CPF ou CNPJ do fornecedor. Formato: '000.000.000-00' para CPF e '00.000.000/0000-00' para CNPJ."
    )
    telefone = serializers.CharField(
        required=False,
        help_text="Número de telefone. Exemplo: '(11) 1234-5678'"
    )
    celular = serializers.CharField(
        required=False,
        help_text="Número de celular. Exemplo: '(11) 91234-5678'"
    )
    email = serializers.EmailField(
        required=False,
        help_text="Email de contato do fornecedor. Exemplo: 'fornecedor@example.com'"
    )

    class Meta:
        model = Fornecedores
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    fornecedor = serializers.PrimaryKeyRelatedField(queryset=Fornecedores.objects.all(), allow_null=True)
    grupo = serializers.PrimaryKeyRelatedField(queryset=GrupoProduto.objects.all(), allow_null=True)
    familia = serializers.PrimaryKeyRelatedField(queryset=FamiliaProduto.objects.all(), allow_null=True)

    cod_produto = serializers.CharField(
        max_length=20,
        help_text="Código único do produto. Exemplo: 'PRD12345'"
    )
    descricao = serializers.CharField(
        max_length=255,
        help_text="Descrição do produto. Exemplo: 'Produto de teste'"
    )
    estoque = serializers.IntegerField(
        help_text="Quantidade atual em estoque. Exemplo: 100"
    )
    custo = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Custo do produto. Exemplo: 12.50"
    )
    venda = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Preço de venda do produto. Exemplo: 20.00"
    )
    tamanho = serializers.CharField(
        max_length=50,
        required=False,
        help_text="Tamanho do produto. Exemplo: 'M'"
    )
    cor = serializers.CharField(
        max_length=50,
        required=False,
        help_text="Cor do produto. Exemplo: 'Azul'"
    )
    peso = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        help_text="Peso do produto em kg. Exemplo: 1.5"
    )

    class Meta:
        model = Produtos
        fields = '__all__'



class GrupoProdutoSerializer(serializers.ModelSerializer):

    nome_grupo = serializers.CharField(
        max_length=255,
        help_text="Nome do grupo de produtos. Exemplo: 'Eletrônicos'"
    )
    sub_grupo_nivel_1 = serializers.CharField(
        max_length=255,
        required=False,
        help_text="Nome do subgrupo de nível 1. Exemplo: 'Computadores'"
    )
    sub_grupo_nivel_2 = serializers.CharField(
        max_length=255,
        required=False,
        help_text="Nome do subgrupo de nível 2. Exemplo: 'Notebooks'"
    )

    class Meta:
        model = GrupoProduto
        fields = '__all__'

class FamiliaProdutoSerializer(serializers.ModelSerializer):

    nome_familia = serializers.CharField(
        max_length=255,
        help_text="Nome da família de produtos. Exemplo: 'Informática'"
    )
    sub_familia = serializers.CharField(
        max_length=255,
        required=False,
        help_text="Nome da subfamília de produtos. Exemplo: 'Periféricos'"
    )

    class Meta:
        model = FamiliaProduto
        fields = '__all__'

class MovimentarEstoqueSerializer(serializers.ModelSerializer):

    tipo_movimentacao = serializers.ChoiceField(
        choices=[('entrada', 'Entrada'), ('saida', 'Saída')],
        help_text="Tipo de movimentação no estoque: 'Entrada' ou 'Saída'."
    )
    data_movimentacao = serializers.DateField(
        help_text="Data da movimentação. Exemplo: '2023-05-20'"
    )
    quantidade = serializers.IntegerField(
        help_text="Quantidade de produtos movimentados. Exemplo: 20"
    )
    descricao_movimentacao = serializers.CharField(
        max_length=255,
        help_text="Descrição da movimentação de estoque. Exemplo: 'Compra de produtos'"
    )

    class Meta:
        model = MovimentarEstoque
        fields = '__all__'

class NumeroSerieSerializer(serializers.ModelSerializer):

    numero_serie = serializers.CharField(
        max_length=100,
        help_text="Número de série do produto. Exemplo: 'SN123456789'"
    )
    nf_compra = serializers.CharField(
        max_length=50,
        required=False,
        help_text="Número da nota fiscal de compra. Exemplo: 'NF123456'"
    )

    class Meta:
        model = NumeroSerie
        fields = '__all__'