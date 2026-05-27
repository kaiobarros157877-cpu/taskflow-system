# src/auth.py

# Dicionário com usuários pré-cadastrados
usuarios = {
    "admin": "123456",
    "kaio": "senha123",
    "operador": "logistica2026"
}

# Lista para armazenar usuários logados
usuarios_logados = []


def cadastrar_usuario(nome, senha):
    """
    Cadastra um novo usuário no sistema.
    """

    # Verifica se o usuário já existe
    if nome in usuarios:
        print("Usuário já cadastrado.")
        return False

    # Adiciona o novo usuário no dicionário
    usuarios[nome] = senha

    print(f"Usuário '{nome}' cadastrado com sucesso.")
    return True


def fazer_login(nome, senha):
    """
    Realiza o login do usuário.
    Retorna True se login válido e False se inválido.
    """

    # Verifica se o usuário existe
    if nome not in usuarios:
        print("Usuário não encontrado.")
        return False

    # Verifica se a senha está correta
    if usuarios[nome] != senha:
        print("Senha incorreta.")
        return False

    # Adiciona o usuário na lista de logados
    if nome not in usuarios_logados:
        usuarios_logados.append(nome)

    print(f"Usuário '{nome}' logado com sucesso.")
    return True


def logout(nome):
    """
    Realiza o logout do usuário.
    """

    # Verifica se o usuário está logado
    if nome in usuarios_logados:
        usuarios_logados.remove(nome)
        print(f"Usuário '{nome}' deslogado com sucesso.")
        return True

    print(f"Usuário '{nome}' não está logado.")
    return False


if __name__ == "__main__":

    # Exibindo usuários iniciais
    print("\n=== USUÁRIOS CADASTRADOS ===")
    print(usuarios)

    # Cadastrando novo usuário
    print("\n=== CADASTRO ===")
    cadastrar_usuario("novo_usuario", "senha789")

    # Tentando login válido
    print("\n=== LOGIN VÁLIDO ===")
    fazer_login("novo_usuario", "senha789")

    # Tentando login inválido
    print("\n=== LOGIN INVÁLIDO ===")
    fazer_login("novo_usuario", "senha_errada")

    # Exibindo usuários logados
    print("\n=== USUÁRIOS LOGADOS ===")
    print(usuarios_logados)

    # Realizando logout
    print("\n=== LOGOUT ===")
    logout("novo_usuario")

    # Exibindo usuários logados após logout
    print("\n=== USUÁRIOS LOGADOS APÓS LOGOUT ===")
    print(usuarios_logados)
