from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CadastroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


usuarios = User.objects.all()


def landpage(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        texto = request.POST.get('mensagem')

        if request.user.is_authenticated:
            Mensagem.objects.create(
                usuario=request.user,
                nome=nome, 
                email=email, 
                mensagem=texto
            )
            messages.success(request, "Mensagem enviada com sucesso!")
        else:
            messages.error(request, "Você precisa estar logado para enviar mensagens.")
            
        return redirect('sac_academia:landpage')

    return render(request, 'sac_academia/landpage.html')



@login_required(login_url='sac_academia:login')
def painel(request):
    if not request.user.is_superuser:
        return redirect('sac_academia:landpage')
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'sac_academia/painel.html', {'mensagens': mensagens})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático
            return redirect('sac_academia:landpage')
    else:
        form = CadastroForm()

    return render(request, 'sac_academia/cadastro.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sac_academia:landpage')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'sac_academia/login.html')



def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('sac_academia:landpage')
