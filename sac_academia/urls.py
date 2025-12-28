from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'sac_academia'

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('login/', LoginView.as_view(template_name='sac_academia/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='sac_academia:landpage'), name='logout'),
    path('painel/', views.painel, name='painel'),
    path('mensagem/deletar/<int:id>/', views.deletar_mensagem, name='deletar_mensagem'),
    path('mensagem/lida/<int:id>/', views.marcar_lida, name='marcar_lida'),
    path('cadastro/', views.cadastro, name='cadastro'),
]