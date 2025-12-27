from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem
from django.contrib.auth.decorators import login_required


def landpage(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        texto = request.POST.get('mensagem')
        if nome and email and texto:
            Mensagem.objects.create(nome=nome, email=email, mensagem=texto)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('sac_academia:landpage')
        messages.error(request, 'Preencha todos os campos.')
    return render(request, 'sac_academia/landpage.html') 



@login_required(login_url='sac_academia:login')
def painel(request):
    if not request.user.is_superuser:
        return redirect('sac_academia:login')
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'sac_academia/painel.html', {'mensagens': mensagens})
