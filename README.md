# Agenda Médica

Sistema desenvolvido como solução para o teste técnico utilizando **Flask**, **SQLAlchemy**, **Flask-Login**, **Flask-Migrate**, **Tabulator.js** e **Docker**.

A aplicação simula uma agenda médica onde um usuário autenticado pode visualizar uma lista de agendamentos obtidos por meio de uma API HTTP.


# Tecnologias Utilizadas

- Python 3.13
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- SQLite
- HTML5
- CSS3
- JavaScript
- Tabulator.js
- Docker
- Docker Compose
- Pytest

<br>

# Funcionalidades

- Autenticação de usuários
- Proteção de rotas utilizando Flask-Login
- API HTTP para consulta dos agendamentos
- Listagem dos agendamentos utilizando Tabulator.js
- Pesquisa dinâmica por:
  - Paciente
  - CPF
  - Médico
  - Especialidade
- Paginação da tabela
- Banco de dados criado automaticamente através das migrations
- População automática do banco com dados de exemplo
- Testes automatizados

<br>

# 📁 Estrutura do Projeto

```text
agenda_medica/
│
├── app
│   ├── agenda/
│   ├── api_mock/
│   ├── auth/
│   ├── commands/
│   ├── models/
│   ├── static/
│   ├── templates/
│   ├── tests/
│   ├── ...
│   
│
├── migrations/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
└── README.md
```

<br>

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/MarivaldoDev/agenda_medica.git

cd agenda_medica
```

## 2. Configure as variáveis de ambiente

Renomeie o arquivo `.env.example` para `.env`.

No Linux/macOS:

```bash
cp .env.example .env
```

No Windows:

```powershell
copy .env.example .env
```

Não é necessário alterar nenhuma variável para executar o projeto.

## 3. Execute a aplicação

```bash
docker compose up --build
```

Na primeira execução o Docker irá automaticamente:

- Criar o banco de dados;
- Executar as migrations;
- Popular o banco com dados de exemplo;
- Inicializar a aplicação.

Após a inicialização acesse:

```
http://localhost:5000
```

<br>

# Credenciais

**Usuário**

```bash
admin
```

**Senha**

```bash
123456
```

<br>

# API

Após realizar o login, a interface busca os dados realizando uma requisição HTTP para:

```bash
GET /api/schedules
```

Exemplo de resposta:

```json
[
  {
    "id": 1,
    "patient": "Maria Silva",
    "cpf": "123.456.789-00",
    "doctor": "Dr. João",
    "specialty": "Cardiologia",
    "date": "2026-07-20",
    "time": "08:30",
    "insurance": "Unimed",
    "status": "Agendado"
  }
]
```

Cada agendamento contém:

- Paciente
- CPF
- Médico
- Especialidade
- Data
- Horário
- Convênio
- Status

<br>

# Executando os Testes

Para executar os testes automatizados:

```bash
pytest
```

Foram implementados testes para os seguintes cenários:

- ✅ Login com credenciais válidas;
- ✅ Login com credenciais inválidas;
- ✅ Retorno da API contendo agendamentos;
- ✅ Retorno da API quando não existem agendamentos.

<br>

# Decisões de Implementação

## Application Factory

A aplicação foi estruturada utilizando o padrão **Application Factory**, reduzindo o acoplamento entre os módulos e facilitando a escalabilidade da aplicação.

As extensões do Flask são inicializadas separadamente e registradas durante a criação da aplicação.

<br>

## Autenticação

A autenticação foi implementada utilizando **Flask-Login**, protegendo o acesso à interface principal da aplicação.

<br>

## API

Conforme solicitado no desafio, os dados apresentados na interface **não são carregados diretamente pelo template**.

Após a autenticação, o navegador realiza uma requisição HTTP para:

```http
GET /api/schedules
```

Os dados retornados são consumidos pelo JavaScript e exibidos utilizando **Tabulator.js**.

<br>

## Banco de Dados

Foi utilizado SQLite juntamente com Flask-Migrate.

Durante a inicialização do container são executados automaticamente:

- Migrations;
- Seed do banco de dados.

Dessa forma nenhuma configuração manual é necessária após executar o Docker.

<br>

# Interface

A listagem foi construída utilizando **Tabulator.js**, oferecendo:

- Paginação;
- Pesquisa dinâmica;
- Organização em tabela;
- Carregamento dos dados via API.

<br>

# Considerações Finais

Busquei desenvolver uma solução simples, organizada e próxima de uma aplicação real, priorizando:

- Organização do código;
- Separação de responsabilidades;
- Utilização do padrão Application Factory;
- Boas práticas com Flask;
- Testes automatizados;
- Facilidade de execução utilizando Docker;
- Código legível e de fácil manutenção.

Agradeço pela oportunidade de participar deste processo seletivo e pela avaliação deste projeto.
