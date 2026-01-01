from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mensagem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CadastroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.paginator import Paginator



usuarios = User.objects.all()


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Mensagem

def landpage(request):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.error(request, "Você precisa estar logado para enviar mensagens.")
            return redirect('sac_academia:login')

        texto = request.POST.get('mensagem')

        if not texto:
            messages.error(request, "A mensagem não pode estar vazia.")
            return redirect('sac_academia:landpage')

        Mensagem.objects.create(
            usuario=request.user,
            nome=request.user.first_name or request.user.username,
            email=request.user.email,
            mensagem=texto
        )

        messages.success(request, "Mensagem enviada com sucesso!")
        return redirect('sac_academia:landpage')

    return render(request, 'sac_academia/landpage.html')




@login_required(login_url='sac_academia:login')
def painel(request):

    if not request.user.is_superuser:
        return redirect('sac_academia:landpage')

    mensagens = Mensagem.objects.all().order_by('-data_envio')

    q = request.GET.get('q')
    data_inicio = request.GET.get('data_inicio')

    if q:
        mensagens = mensagens.filter(
            Q(nome__icontains=q) |
            Q(email__icontains=q) |
            Q(mensagem__icontains=q)
        )

    if data_inicio:
        mensagens = mensagens.filter(
            data_envio__date=data_inicio
        )

    paginator = Paginator(mensagens, 10)  # 10 por página
    page_number = request.GET.get('page')
    mensagens_paginadas = paginator.get_page(page_number)

    return render(request, 'sac_academia/painel.html', {
        'mensagens': mensagens_paginadas
    })


@login_required(login_url='sac_academia:login')
def deletar_mensagem(request, id):
    if not request.user.is_superuser:
        return redirect('sac_academia:landpage')
    
    mensagem = get_object_or_404(Mensagem, id=id)
    mensagem.delete()
    messages.success(request, "Mensagem excluída com sucesso!")
    return redirect('sac_academia:painel')

@login_required(login_url='sac_academia:login')
def marcar_lida(request, id):
    if not request.user.is_superuser:
        return redirect('sac_academia:landpage')
    
    mensagem = get_object_or_404(Mensagem, id=id)
    mensagem.lida = True 
    mensagem.save()
    return redirect('sac_academia:painel')


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('sac_academia:landpage')
    else:
        form = CadastroForm()

    return render(request, 'sac_academia/cadastro.html', {'form': form})





