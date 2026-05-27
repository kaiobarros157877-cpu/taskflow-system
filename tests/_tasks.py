# tests/test_tasks.py

# Importações necessárias
import sys
import os

# Adiciona a pasta src ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Importando funções do sistema de tarefas
from app import (
    criar_tarefa,
    listar_tarefas,
    listar_por_prioridade,
    atualizar_tarefa,
    excluir_tarefa,
    tarefas
)

# Importando função de login
from auth import fazer_login


def setup_function():
    """
    Função executada antes de cada teste.
    Limpa a lista de tarefas para evitar interferência entre testes.
    """

    tarefas.clear()


def test_criar_tarefa():
    """
    Verifica se a tarefa é criada corretamente
    com todos os campos esperados.
    """

    tarefa = criar_tarefa(
        "Teste",
        "Descrição de teste",
        "alta"
    )

    assert tarefa["titulo"] == "Teste"
    assert tarefa["descricao"] == "Descrição de teste"
    assert tarefa["prioridade"] == "alta"
    assert tarefa["status"] == "A Fazer"
    assert "id" in tarefa


def test_listar_tarefas():
    """
    Verifica se a função retorna uma lista.
    """

    criar_tarefa(
        "Tarefa 1",
        "Descrição",
        "normal"
    )

    resultado = listar_tarefas()

    assert isinstance(resultado, list)


def test_atualizar_status():
    """
    Verifica se o status da tarefa
    é atualizado corretamente.
    """

    tarefa = criar_tarefa(
        "Entrega",
        "Separar pedidos",
        "alta"
    )

    atualizar_tarefa(tarefa["id"], "Concluído")

    assert tarefa["status"] == "Concluído"


def test_excluir_tarefa():
    """
    Verifica se a tarefa é removida da lista.
    """

    tarefa = criar_tarefa(
        "Excluir",
        "Teste de exclusão",
        "baixa"
    )

    resultado = excluir_tarefa(tarefa["id"])

    assert resultado is True
    assert len(tarefas) == 0


def test_filtrar_por_prioridade():
    """
    Verifica se o filtro por prioridade
    retorna apenas tarefas da prioridade informada.
    """

    criar_tarefa(
        "Tarefa Alta",
        "Prioridade alta",
        "alta"
    )

    criar_tarefa(
        "Tarefa Normal",
        "Prioridade normal",
        "normal"
    )

    resultado = listar_por_prioridade("alta")

    assert len(resultado) == 1
    assert resultado[0]["prioridade"] == "alta"


def test_login_valido():
    """
    Verifica se o login funciona corretamente
    com usuário e senha válidos.
    """

    resultado = fazer_login("admin", "123456")

    assert resultado is True


def test_login_invalido():
    """
    Verifica se o sistema rejeita
    uma senha incorreta.
    """

    resultado = fazer_login("admin", "senha_errada")

    assert resultado is False
