# src/app.py

# Lista global para armazenar as tarefas
tarefas = []

# Variável global para controle de IDs
contador_id = 1


def criar_tarefa(titulo, descricao, prioridade):
    """
    Cria uma nova tarefa e adiciona na lista de tarefas.
    """

    global contador_id

    # Validação das prioridades permitidas
    prioridades_validas = ["baixa", "normal", "alta"]

    if prioridade.lower() not in prioridades_validas:
        raise ValueError("Prioridade inválida. Use: baixa, normal ou alta.")

    # Estrutura da tarefa
    tarefa = {
        "id": contador_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade.lower(),
        "status": "A Fazer"
    }

    # Adiciona a tarefa na lista
    tarefas.append(tarefa)

    # Incrementa o contador de ID
    contador_id += 1

    return tarefa


def listar_tarefas():
    """
    Retorna todas as tarefas cadastradas.
    """

    return tarefas


def listar_por_prioridade(prioridade):
    """
    Filtra tarefas pela prioridade informada.
    """

    return [
        tarefa
        for tarefa in tarefas
        if tarefa["prioridade"] == prioridade.lower()
    ]


def atualizar_tarefa(id, novo_status):
    """
    Atualiza o status de uma tarefa pelo ID.
    """

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["status"] = novo_status
            return tarefa

    return None


def excluir_tarefa(id):
    """
    Remove uma tarefa da lista pelo ID.
    """

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return True

    return False


if __name__ == "__main__":

    # Criando tarefas de exemplo
    tarefa1 = criar_tarefa(
        "Separar pedidos",
        "Separar os produtos do estoque",
        "alta"
    )

    tarefa2 = criar_tarefa(
        "Atualizar sistema",
        "Atualizar status das entregas",
        "normal"
    )

    tarefa3 = criar_tarefa(
        "Organizar estoque",
        "Reorganizar prateleiras do depósito",
        "baixa"
    )

    # Exibindo todas as tarefas
    print("\n=== TODAS AS TAREFAS ===")
    for tarefa in listar_tarefas():
        print(tarefa)

    # Filtrando tarefas por prioridade
    print("\n=== TAREFAS DE PRIORIDADE ALTA ===")
    tarefas_alta = listar_por_prioridade("alta")

    for tarefa in tarefas_alta:
        print(tarefa)

    # Atualizando status de uma tarefa
    print("\n=== ATUALIZANDO STATUS ===")
    atualizar_tarefa(1, "Em Andamento")

    print(listar_tarefas())

    # Excluindo uma tarefa
    print("\n=== EXCLUINDO TAREFA ===")
    excluir_tarefa(2)

    # Exibindo lista final
    print("\n=== LISTA FINAL DE TAREFAS ===")
    for tarefa in listar_tarefas():
        print(tarefa)
