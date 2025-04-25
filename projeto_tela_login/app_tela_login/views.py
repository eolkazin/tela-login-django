from django.shortcuts import render, redirect  # Importa as funções render e redirect
from django.contrib.auth.models import User  # Usando o modelo padrão de User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import Usuario


###CRIAÇÃO DA VIEW DE LOGIN###
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Tenta autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se o usuário for autenticado com sucesso
            login(request, user)
            return redirect(
                "home"
            )  # Redireciona para a página inicial (ou qualquer outra página)
        else:
            # Se a autenticação falhar
            error_message = "Credenciais inválidas"
            return render(
                request, "T_login/login.html", {"error_message": error_message}
            )

    return render(request, "T_login/login.html")


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        # Verificar se as senhas coincidem
        if password != password_confirm:
            error_message = "As senhas não coincidem."
            return render(
                request, "T_login/cadastro.html", {"error_message": error_message}
            )

        # Verificar se o nome de usuário já existe
        if Usuario.objects.filter(username=username).exists():
            error_message = "Nome de usuário já existe."
            return render(
                request, "T_login/cadastro.html", {"error_message": error_message}
            )

        # Criptografar a senha e salvar o usuário
        password_hash = make_password(password)
        usuario = Usuario(username=username, password=password_hash)
        usuario.save()

        return redirect("login")  # Redireciona para a página de login após o cadastro

    return render(request, "T_login/cadastro.html")
