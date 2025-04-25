# 🛡️ Projeto Django de Autenticação de Usuários com Criptografia Segura

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/seu-usuario/seu-repositorio/graphs/commit-activity)

Este projeto Django oferece uma **implementação completa, robusta e segura** de um sistema de autenticação de usuários, priorizando as melhores práticas de desenvolvimento web e a proteção das informações. Ele integra uma interface de login amigável e emprega a **criptografia de senhas de nível empresarial** diretamente no banco de dados através da função `make_password` do Django. Essa abordagem garante a confidencialidade das credenciais dos usuários contra ameaças comuns.

## ✨ Funcionalidades em Destaque:

* **🔑 Interface de Login Intuitiva e Personalizável:** Uma tela de login HTML bem estruturada, com design limpo e de fácil adaptação para a identidade visual da sua aplicação.
* **🔒 Autenticação Robusta e Segura:** Mecanismo de autenticação backend confiável que verifica as credenciais fornecidas com os registros de usuários armazenados de forma protegida no banco de dados.
* **🛡️ Criptografia de Senhas de Última Geração:** Utilização da função `make_password` do Django, que emprega algoritmos de hash seguros e modernos (como **PBKDF2** ou **Argon2**, dependendo da configuração do Django) juntamente com **_salt_** aleatórios exclusivos por usuário. Isso impede o armazenamento de senhas em texto plano e oferece defesa sólida contra ataques de dicionário e tabelas _rainbow_.
* **✅ Validação de Formulário Integrada no Servidor:** Implementação de validação robusta no lado do servidor para garantir que os dados de login atendam aos critérios definidos, prevenindo a entrada de dados maliciosos e erros de submissão.
* **💬 Feedback ao Usuário Claro e Informativo:** Exibição de mensagens de erro contextuais e amigáveis em cenários de autenticação falha (ex: "Nome de usuário ou senha inválidos. Por favor, tente novamente.").
* **➡️ Redirecionamento Pós-Login Inteligente:** Após a autenticação bem-sucedida, o usuário é automaticamente redirecionado para uma página específica e relevante, otimizando o fluxo de navegação e a experiência do usuário.
* **🚪 Logout Seguro e Confiável:** Mecanismo de logout implementado para encerrar a sessão do usuário de forma segura, protegendo contra o sequestro de sessão e garantindo a privacidade.
* **🏗️ Estrutura de Código Organizada e de Fácil Manutenção:** O projeto segue rigorosamente as convenções de estrutura de diretórios do Django, promovendo a legibilidade, a manutenibilidade, a escalabilidade e a colaboração eficiente.
* **🌐 Foco em Práticas de Codificação Segura:** O desenvolvimento foi realizado com atenção especial às melhores práticas de segurança, visando mitigar vulnerabilidades comuns em aplicações web e proteger os dados dos usuários.

## ⚙️ Pré-requisitos Essenciais:

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

* **🐍 Python:** Versão **3.8 ou superior** (altamente recomendada para aproveitar os recursos mais recentes e melhorias de segurança). Para verificar sua versão:
    ```bash
    python --version
    ```
* **<0xF0><0x9F><0xAA><0x9E> Django:** Versão **4.0 ou superior** (recomendada para obter os mais recentes recursos de segurança e funcionalidades aprimoradas). Instale com:
    ```bash
    pip install Django
    ```
* **📦 pip:** O gerenciador de pacotes padrão do Python, geralmente incluído com a instalação do Python. Mantenha-o atualizado:
    ```bash
    pip install --upgrade pip
    ```

## 🚀 Instruções Detalhadas de Instalação e Execução:

Siga estas etapas para configurar e executar o projeto em seu ambiente local:

1.  **📥 Clonar o Repositório (se aplicável):**
    Se o código estiver em um repositório Git, clone-o para sua máquina:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <nome_do_projeto>
    ```

2.  **<0xF0><0x9F><0xA7><0xAE> Configurar o Ambiente Virtual:**
    É altamente recomendável criar um ambiente virtual isolado para este projeto:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Em sistemas Unix/macOS
    .venv\Scripts\activate   # Em sistemas Windows
    ```

3.  **⬇️ Instalar as Dependências:**
    Se houver um arquivo `requirements.txt` listando as dependências do projeto, instale-as com:
    ```bash
    pip install -r requirements.txt
    ```
    Caso contrário, para este projeto básico de autenticação, você pode precisar apenas do Django (já instalado no passo anterior).

4.  **⚙️ Configurar o Banco de Dados:**
    Edite o arquivo de configurações do Django (`projeto_tela_login/settings.py`) para personalizar as opções do seu banco de dados. Por padrão, o Django utiliza o SQLite, que é adequado para desenvolvimento. Para ambientes de produção, considere utilizar bancos de dados mais robustos como PostgreSQL, MySQL ou outros.

5.  **<0xF0><0x9F><0x95><0xB3>️ Aplicar as Migrações:**
    Este comando sincroniza os modelos de dados definidos em sua aplicação (`app_tela_login/models.py`) com o esquema do banco de dados:
    ```bash
    python manage.py migrate
    ```

6.  **👤 Criar um Superusuário:**
    Use este comando para criar uma conta de administrador com privilégios totais para acessar o painel administrativo do Django:
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir um nome de usuário, endereço de e-mail e senha para o superusuário.

7.  **🚀 Iniciar o Servidor de Desenvolvimento:**
    Execute o servidor de desenvolvimento do Django para testar a aplicação localmente:
    ```bash
    python manage.py runserver 0.0.0.0:8000   # Para acessar de outras máquinas na rede, se necessário
    ```
    Por padrão, o servidor estará rodando em `http://127.0.0.1:8000/`.

8.  **🌐 Acessar a Aplicação:**
    Abra seu navegador web e navegue até a URL configurada para a tela de login. Geralmente, a URL da tela de login é definida no arquivo `projeto_tela_login/urls.py` ou no `urls.py` da sua aplicação (`app_tela_login/urls.py`).

## 📂 Estrutura Detalhada do Projeto:

projeto_tela_login/                 # 📂 Diretório raiz do projeto Django
├── app_tela_login/                 # 📂 Aplicação Django para a tela de login
│   ├── migrations/                 # 📂 Arquivos de migração do banco de dados
│   ├── static/                     # 📂 Arquivos estáticos (CSS, JavaScript, imagens)
│   │   └── css/
│   │       └── login.css
│   ├── templates/                  # 📂 Templates HTML
│   │   └── app_tela_login/
│   │       └── login.html
│   ├── init.py
│   ├── admin.py                    # 📄 Configurações do painel de administração
│   ├── apps.py                     # 📄 Configuração da aplicação
│   ├── forms.py                    # 📄 Formulários Django (incluindo o formulário de login)
│   ├── models.py                   # 📄 Definição dos modelos de dados
│   ├── tests.py                    # 📄 Testes unitários e de integração
│   └── views.py                    # 📄 Lógica de controle da aplicação (views)
├── projeto_tela_login/             # 📂 Diretório de configurações do projeto Django
│   ├── init.py
│   ├── asgi.py                     # 📄 Configuração para servidores ASGI
│   ├── settings.py                 # 📄 Arquivo de configurações do projeto
│   ├── urls.py                     # 📄 Definições de URL do projeto
│   └── wsgi.py                     # 📄 Configuração para servidores WSGI
├── db.sqlite3                      # 💾 Arquivo de banco de dados SQLite (padrão)
├── manage.py                       # ⚙️ Script utilitário de gerenciamento do Django
├── requirements.txt                # 📄 Lista de dependências do projeto
├── .gitignore                      # 📄 Especifica arquivos ignorados pelo Git
└── .venv/                          # 📂 Diretório do ambiente virtual