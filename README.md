<img src="logo.png" alt="Mupi Systems Logo" width="200"/>

# 🚀 Teste Técnico - Estágio Desenvolvedor Full Stack

---

## 📖 Sobre o Teste

Bem-vindo(a) ao teste técnico para a vaga de **Estágio em Desenvolvimento Full Stack** na Mupi Systems!

### O que você vai construir?

Você irá desenvolver uma **aplicação web simples** usando Django que consiste em:

1. **Uma landpage pública** - Página inicial com informações sobre um produto/serviço de sua escolha e um formulário de contato
2. **Um sistema de mensagens** - As mensagens enviadas pelo formulário serão salvas no banco de dados
3. **Uma área administrativa** - Onde você (admin) poderá visualizar todas as mensagens recebidas através de login

### Como funciona?

```
┌─────────────────────────────────────────────────────────────┐
│  VISITANTE                                                  │
│  ↓                                                          │
│  Acessa a landpage → Preenche formulário (nome, email,      │
│  mensagem) → Clica em "Enviar" → Mensagem salva no banco    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  ADMINISTRADOR                                              │
│  ↓                                                          │
│  Acessa /painel → Faz login (superusuário) → Visualiza      │
│  lista com todas as mensagens (nome, email, mensagem, data) │
└─────────────────────────────────────────────────────────────┘
```

### O que esperamos?

- ✅ Código funcional (mesmo que simples)
- ✅ Organização básica do projeto Django
- ✅ Formulário salvando dados corretamente
- ✅ Interface responsiva e limpa
- ✅ README com instruções para rodar o projeto


---

## 🎯 Objetivos

- Desenvolver uma **landpage** simples com formulário de contato funcional
- Visualizar mensagens recebidas em uma área administrativa
- Demonstrar conhecimentos básicos em **Django** e **frontend**
- Mostrar capacidade de aprendizado e organização de código
- Criar uma interface responsiva e funcional

---

## 📋 Instruções

### 🔀 Fork do Repositório

1. Faça um **fork** deste repositório para sua conta pessoal do GitHub
2. Trabalhe em seu próprio fork

### 💻 Implementação

- Desenvolva o projeto conforme os requisitos abaixo
- Use **Django** e **Django Templates** como base
- Utilize **TailwindCSS** para estilização

### 📤 Submissão

1. Após finalizar, abra um **Pull Request** do seu fork para o repositório original
2. Aguarde o agendamento da reunião para avaliação do teste

### 📝 Documentação

Inclua um arquivo `README.md` com:
- ✅ Descrição do projeto
- ✅ Passo a passo para rodar a aplicação
- ✅ Tecnologias utilizadas

---

## 🛠️ Requisitos Técnicos Mínimos

### 🐍 Backend (Django)

| Requisito | Descrição |
|-----------|-----------|
| **Versão do Django** | 4.0 ou superior |
| **Templates Obrigatórios** | • `landpage.html` - Página inicial com informações do produto e formulário de contato<br>• `login.html` - Tela de login customizada<br>• `painel.html` - Painel administrativo para listar mensagens |
| **Model** | Mensagem com campos: `nome`, `email`, `mensagem`, `data_envio` |
| **Autenticação** | Usar o sistema de autenticação do Django (criar superusuário) |
| **Funcionalidades** | • Salvar mensagens do formulário no banco<br>• Login com superusuário criado<br>• Visualizar mensagens em painel customizado protegido por login |
| **Views e URLs** | • View para landpage com informações do produto e formulário de contato<br>• View de login customizada<br>• View protegida (`@login_required`) para o painel de mensagens |

### 🎨 Frontend

#### Tecnologias

- **TailwindCSS** ou **CSS puro** - Para estilização
- **Django Templates** - Para renderização de páginas

#### Requisitos de Interface

- Design **responsivo** básico (mobile e desktop)
- Formulário **funcional** na landpage
- Lista de mensagens organizada na área admin

### 🧹 Qualidade de Código

- Código **organizado** e legível
- Estrutura de projeto Django **básica** funcionando
- README com instruções claras

---

## 🎨 Critérios de Avaliação

### Funcionalidade
- Formulário salvando mensagens no banco de dados
- Listagem de mensagens funcionando
- Sistema de login protegendo a área administrativa

### Qualidade de Código
- Código organizado e legível
- Estrutura Django adequada
- Boas práticas básicas do Python/Django

### Interface
- Layout limpo e organizado
- Responsividade básica
- Formulário com boa usabilidade

### Documentação
- README com instruções claras
- Código com comentários quando necessário

---

## ✨ Diferenciais (Bônus)

Estes elementos são **totalmente opcionais** e darão pontos extras:

### Design e UX
- 🎨 **Visual atraente** - Uso de cores e tipografia harmoniosas, numa landpage bonita e bem feita - esse é o maior diferencial


### Funcionalidades Extras
- 🔔 **Validação de formulários** - Validações no frontend e backend
- 🔄 **Feedback visual** - Mensagens de sucesso/erro nas ações
- 🎯 **Usar HTMX ou Alpine.js** - Adicionar interatividade moderna
- 📊 **Filtros ou busca** - Filtrar mensagens por data ou texto no painel
- ✏️ **Editar/Excluir mensagens** - Adicionar ações de CRUD no painel
- 📧 **Campos adicionais no model** - Como telefone, assunto, status, etc.
- � **Paginação** - Adicionar paginação na listagem de mensagens
- 🎨 **Estilização avançada** - Design mais elaborado no painel administrativo

---

## 💡 Diretrizes Criativas

### 🌐 Landpage

> **Liberdade criativa!** Escolha qualquer tema de produto/serviço (pode ser real ou fictício)

**Sugestões de temas:**
- 📱 Aplicativo mobile 
- 🏋️ Academia
- 🍕 Restaurante
- 💼 Agência de marketing
-  Plataforma de cursos
- � Software house
- Ou qualquer outro tema de sua preferência!

#### Elementos Essenciais da Landpage

| Seção | Descrição |
|-------|-----------|
| **Header** | Logo/título e menu simples |
| **Hero Section** | Banner principal com título e chamada |
| **Sobre/Features** | Breve descrição do produto/serviço |
| **Formulário de Contato** | Form funcional com campos: nome, email, mensagem |
| **Footer** | Informações básicas de rodapé |

---

## 🎨 Exemplos Visuais de Inspiração

Na pasta [`examples/`](./examples) você encontrará **exemplos visuais** de design que podem servir como **inspiração** para suas interfaces:

### 📸 O que tem na pasta:

- **`landpage_1.jpg`, `landpage_2.jpg`, `landpage_3.jpg`** - Exemplos de design de landpages
- **`login_1.jpg`, `login_2.jpg`, `login_3.jpg`** - Exemplos de telas de login

💡 **Como usar:**
- Use como **referência visual** para criar seu próprio design
- Você **NÃO precisa copiar** esses designs exatamente
- Sinta-se livre para criar algo completamente diferente
- O importante é ter uma interface **limpa, organizada e funcional**

🎯 **Dica:** Analise os exemplos para entender elementos como layout, cores, espaçamento e hierarquia visual!

---

### 🔐 Área Administrativa

Você deve criar um **painel administrativo customizado** para visualizar as mensagens recebidas, utilizando o sistema de autenticação do Django para controlar o acesso.

#### Como Implementar

##### 1️⃣ Crie o Superusuário do Django

Após configurar o banco de dados, crie um usuário administrador:

```bash
python manage.py createsuperuser
```

Você será solicitado a fornecer:
- **Username** (nome de usuário)
- **Email** (opcional)
- **Password** (senha - será usada para fazer login)

💡 **Esse usuário será usado para acessar o painel administrativo!**

##### 2️⃣ Configure a View de Login

Use a `LoginView` do Django para criar uma tela de login customizada:

```python
# urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landpage'), name='logout'),
    path('painel/', views.painel_mensagens, name='painel'),
]
```

##### 3️⃣ Crie o Template de Login

Crie `login.html` com um formulário de login. O Django fornecerá o formulário através da variável `form`.

💡 **Dica:** Pesquise sobre `{{ form.as_p }}` ou como renderizar formulários do Django!

##### 4️⃣ Crie a View Protegida do Painel

Crie uma view que exibe as mensagens e proteja-a com `@login_required`:

```python
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Mensagem

@login_required(login_url='login')  # Redireciona para a rota 'login' se não autenticado
def painel_mensagens(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'painel.html', {'mensagens': mensagens})
```

##### 5️⃣ Crie o Template do Painel

Crie `painel.html` com uma listagem das mensagens recebidas. Você pode exibir em tabela, cards, ou qualquer formato que preferir!

💡 **Dica:** Use `{{ user.username }}` para mostrar quem está logado e crie um link de logout!

#### Como Funciona o Fluxo de Autenticação

1. **Visitante** acessa `/painel`
2. Como não está autenticado, o Django **redireciona automaticamente** para `/login`
3. **Admin** faz login com o superusuário criado no `login.html`
4. Após login bem-sucedido, é **redirecionado de volta** para `/painel`
5. Agora consegue ver todas as mensagens!

#### Requisitos Mínimos

- ✅ **Criar superusuário** - Via comando `createsuperuser`
- ✅ **View protegida** - Usar `@login_required` no painel
- ✅ **Templates customizados** - `login.html` e `painel.html`
- ✅ **Login funcional** - Usar `LoginView` do Django
- ✅ **Listar mensagens** - Exibir nome, email, mensagem e data no painel
- ✅ **Logout** - Link ou botão para fazer logout

💡 **Vantagem:** Você cria templates do seu jeito, mas usa o sistema de autenticação já pronto do Django!

---

## 📁 Estrutura Sugerida

```text
pasta raiz do projeto/
├── README.md
├── requirements.txt
├── manage.py
├── core/
│   ├── settings.py
│   └── urls.py
├── contato/  (ou outro nome)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── landpage.html
│       ├── login.html
│       └── painel.html
└── static/
    ├── css/
    └── images/
```

**Nota:** Esta é apenas uma sugestão. Você pode organizar de forma diferente.

---
## 🚀 Como Rodar a Aplicação

> **💡 Importante:** Inclua estas instruções no README do seu projeto

### Passo a Passo

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

#### 2️⃣ Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5️⃣ Crie um superusuário (para acessar a área admin)
```bash
python manage.py createsuperuser
```

#### 6️⃣ Execute o servidor
```bash
python manage.py runserver
```

#### 7️⃣ Acesse a aplicação

- **Landpage:** `http://localhost:8000`
- **Login:** `http://localhost:8000/login`
- **Painel Administrativo:** `http://localhost:8000/painel` (requer login)

---
## 📝 Notas Importantes

| Aspecto | Observação |
|-----------|--------------|
| **Tempo Estimado** | 6-10 horas para conclusão básica |
| **Foco Principal** | Funcionalidade antes de design elaborado |
| **Ajuda Externa** | Pode consultar documentação oficial do Django |
| **Simplicidade** | Prefira fazer simples e funcional do que complexo e quebrado |

---

## 💭 Não Conseguiu Completar Tudo?

> **Sem problemas!** Entregue o desafio mesmo que incompleto e explique no Pull Request:
> - ✅ O que você conseguiu fazer
> - ✅ Onde teve dificuldades  
> - ✅ O que faria diferente com mais tempo

**Avaliaremos seu raciocínio e esforço!** 😊

---

## 🤖 Sobre o Uso de IA

O uso de **ferramentas de IA** (ChatGPT, GitHub Copilot, Claude, etc.) é **permitido** como auxílio no aprendizado.

### ⚠️ Importante

**Você DEVE ser capaz de:**

- 📖 **Explicar** cada parte do código que você entrega
- 🧠 **Entender** o funcionamento das funcionalidades
- 🔧 **Debugar** problemas que surgirem
- 💬 **Responder perguntas** sobre suas escolhas técnicas

### 💡 Recomendação

Use IA como **ferramenta de aprendizado**, não como substituto. Durante a avaliação, faremos perguntas sobre o código para entender seu nível de compreensão.

**O objetivo é avaliar suas habilidades de aprendizado e raciocínio!** 🚀

---

<div align="center">

### Boa sorte com o teste técnico! 🌟

**Mostre suas habilidades e criatividade!**

</div>
