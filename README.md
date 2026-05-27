# TaskFlow System

Sistema de gerenciamento de tarefas desenvolvido pela TechFlow Solutions para uma startup do setor de logística. O projeto tem como foco organizar atividades operacionais, melhorar o acompanhamento de demandas e otimizar o fluxo de trabalho das equipes.

---

## 📌 Descrição do Projeto

O **TaskFlow System** é uma aplicação desenvolvida para auxiliar equipes de logística no controle e gerenciamento de tarefas diárias. O sistema permite criar, editar, visualizar e excluir tarefas, além de possuir autenticação de usuários para garantir segurança e controle de acesso.

---

## 🎯 Objetivo do Sistema

O principal objetivo do sistema é centralizar o gerenciamento de tarefas operacionais da startup de logística, proporcionando:

- Organização das atividades da equipe
- Controle de execução de tarefas
- Acompanhamento de produtividade
- Redução de falhas operacionais
- Melhor rastreabilidade das demandas internas

---

## 🚀 Escopo Inicial

As funcionalidades previstas na primeira versão do sistema incluem:

### ✅ Funcionalidades Principais

- CRUD completo de tarefas
  - Criar tarefas
  - Listar tarefas
  - Atualizar tarefas
  - Excluir tarefas

- Sistema de autenticação
  - Login de usuários
  - Controle de sessão
  - Validação de acesso

---

## 🛠️ Metodologia Ágil

O projeto utiliza a metodologia ágil **Kanban**, permitindo:

- Visualização do fluxo de trabalho
- Priorização contínua das atividades
- Melhor acompanhamento das entregas
- Organização das tarefas por status

### Fluxo Kanban Utilizado

- Backlog
- A Fazer
- Em Desenvolvimento
- Em Teste
- Concluído

---

## 📂 Estrutura de Diretórios

```bash
TaskFlow-System/
│
├── src/
│   ├── auth/
│   ├── tasks/
│   ├── database/
│   └── main.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_tasks.py
│   └── conftest.py
│
├── docs/
│   ├── requisitos.md
│   ├── arquitetura.md
│   └── sprint-planning.md
│
├── requirements.txt
├── README.md
└── .gitignore

Tecnologias Utilizadas
Python 3.11+
Pytest
SQLite
Git e GitHub

Instalação e Execução Local
Pré-requisitos
Python 3.11 ou superior
Git instalado

1. Clonar o repositório
git clone https://github.com/techflow-solutions/taskflow-system.git

2. Acessar o diretório do projeto
cd taskflow-system

3. Criar ambiente virtual

LInux/MacOS
python -m venv venv
source venv/bin/

WIndows
python -m venv venv
venv\Scripts\activate

4. Instalar dependências
pip install -r requirements.txt

5. Executar o sistema
python src/main.py

Executando os teste
Os testes automatizados são executados utilizando o Pytest.
pytest
pytest -v

Mudança de Escopo

Durante a Sprint 2, surgiu a necessidade de melhorar a organização e visualização das tarefas mais importantes. Como resultado, foi adicionada uma nova funcionalidade ao sistema:

Nova Feature: Filtro por Prioridade

A funcionalidade permite:
Melhorar o planejamento operacional
Visualizar tarefas críticas rapidamente
Filtrar tarefas por nível de prioridade

Impacto da MUdança

Atualização da estrutura de dados
Modificação nas rotas de listagem
Criação de novos testes automatizados
Ajustes no backlog do Kanban

esenvolvido por

Desenvolvido por TechFlow Solutions
Soluções tecnológicas para gestão operacional e automação de processos.

Licença

Este projeto é fictício e foi criado para fins educacionais e demonstração de estrutura de documentação técnica.

