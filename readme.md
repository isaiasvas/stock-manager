
# Stock Manager

![GitHub repo size](https://img.shields.io/github/repo-size/isaiasvas/stock-manager?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/isaiasvas/stock-manager?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/isaiasvas/stock-manager?style=for-the-badge)

> O Stock Manager é uma ferramenta para gerenciar estoques de forma eficiente e automatizada, construída com Django para fornecer uma API robusta e um painel administrativo intuitivo.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações incluirão:

- [x] Criação de API
- [x] Swagger e Redoc
- [ ] Criação de frontend

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de Python (>=3.8)
- Você está utilizando um sistema operacional compatível (Windows, Linux, ou macOS)
- Você leu a documentação do projeto

## 🚀 Instalando Stock Manager

Para instalar o Stock Manager, siga estas etapas:

### Linux e macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

## ☕ Usando Stock Manager

Para usar o Stock Manager, siga estas etapas:

1. Inicie o ambiente virtual conforme as instruções de instalação.
2. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```
   Siga as instruções para definir um nome de usuário, e-mail e senha.

3. Execute o servidor Django:
   ```bash
   python manage.py runserver
   ```

4. Acesse o sistema no navegador:
   - Painel administrativo: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Documentação Swagger: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   - Documentação Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Agora você pode navegar pelo painel administrativo para cadastrar produtos, atualizar quantidades em estoque e gerar relatórios.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
