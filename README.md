# 🏋️ SAC Academia - Sistema de Atendimento ao Cliente

## 📋 Visão Geral

O **SAC Academia** é um sistema de atendimento ao cliente desenvolvido para academias, permitindo que alunos enviem mensagens e dúvidas por meio de uma **landpage**, enquanto os administradores gerenciam essas mensagens através de um **painel administrativo seguro**.

O projeto foi desenvolvido com **Django** e **Django Templates**, seguindo boas práticas de organização, segurança e usabilidade.

---

## ✨ Funcionalidades

### 👤 Para Usuários

* Página inicial (landpage) com informações da academia
* Formulário de contato para envio de mensagens
* Sistema de autenticação para usuários registrados

### 🔐 Para Administradores

* Painel administrativo protegido por login
* Visualização de todas as mensagens recebidas
* Marcar mensagens como lidas/não lidas
* Excluir mensagens
* Gerenciamento de usuários

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Django 4.x+
* **Banco de Dados:** SQLite (ambiente de desenvolvimento)
* **Frontend:** HTML5, TailwindCSS, JavaScript
* **Autenticação:** Sistema nativo de usuários do Django
* **Controle de Versão:** Git

---

## 🚀 Como Executar o Projeto

### 📌 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

* **Python 3.8 ou superior**
* **pip** (gerenciador de pacotes do Python)
* **Git** (opcional, para clonar o repositório)

---

### 📥 Instalação

#### 1️⃣ Clone o repositório

```bash
git clone [URL_DO_REPOSITORIO]
cd projeto_estagio_2026_1
```

> Caso não utilize Git, você pode baixar o projeto como `.zip` e extrair os arquivos.

---

#### 2️⃣ Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv venv
```

Ativação:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

---

#### 3️⃣ Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

---

#### 4️⃣ Execute as migrações do banco de dados

```bash
python manage.py migrate
```

Esse comando cria as tabelas necessárias no banco SQLite.

---

#### 5️⃣ Crie um superusuário (administrador)

```bash
python manage.py createsuperuser
```

Informe:

* Nome de usuário
* Email (opcional)
* Senha

Esse usuário será utilizado para acessar o painel administrativo.

---

### ▶️ Execução do Projeto

#### 6️⃣ Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

---

#### 7️⃣ Acesse a aplicação no navegador

* 🌐 **Landpage:**
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* 🔐 **Painel Administrativo Customizado:**
  [http://127.0.0.1:8000/painel/](http://127.0.0.1:8000/painel/)

* ⚙️ **Admin padrão do Django:**
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

✅ **Pronto!** O sistema estará rodando localmente e pronto para testes.



## 🔒 Segurança

* Autenticação obrigatória para acesso ao painel administrativo
* Senhas armazenadas com hashing seguro
* Proteção contra CSRF
* Rotas administrativas protegidas com `@login_required`
