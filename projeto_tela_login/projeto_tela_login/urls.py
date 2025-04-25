from django.urls import path
from app_tela_login import views

urlpatterns = [
    #### ROTA , VIEW, NOME REFERÊNCIA ####
    #### login.com ####
    path("", views.login_view, name="login"),  # Rota para a página de login
    #### cadastro.com ####
    path(
        "cadastro/", views.cadastro, name="cadastro"
    ),  # Rota para a página de cadastro
]
