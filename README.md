# Sistema de Gerenciamento de Biblioteca

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![POO](https://img.shields.io/badge/Paradigm-OOP-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)
![GitHub last commit](https://img.shields.io/github/last-commit/guilherme28-tech/biblioteca-sistema-poo)
![GitHub repo size](https://img.shields.io/github/repo-size/guilherme28-tech/biblioteca-sistema-poo)

Sistema de gerenciamento de biblioteca desenvolvido em Python com foco em boas práticas de backend, organização em camadas e aplicação de POO.

## Sobre o Projeto

Esse projeto foi desenvolvido com o objetivo de praticar:

- POO
- Separação de responsabilidades
- Padrão Repository
- Regras de negócio
- Persistência de dados com SQLite
- Tratamento de erros controlados
- Organização profissional de código backend

O sistema permite gerir usuários, livros e empréstimos, aplicando validações e regras reais de negócio.

---

## Funcionalidades

### Usuários
- Cadastro de usuários
- Listagem de usuários

### Livros
- Cadastro de livros
- Listagem de livros
- Controle de disponibilidade

### Empréstimos
- Realizar empréstimo de livro
- Impedir empréstimo de livro já emprestado
- Devolver livro
- Atualização automática do status do livro

---

## Tecnologias Utilizadas

- Python 3
- SQLite
- POO
- Padrão Repository
- Git e GitHub

---

## Conceitos aplicados

- Classes e objetos
- Encapsulamento
- Métodos de busca
- Controle de estado
- Estrutura modular

## Requisitos

- Python 3.10+

## ⚙️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/guilherme28-tech/biblioteca-sistema-poo.git
```

2. Acesse a pasta:

```
cd biblioteca-sistema-poo
```

3. Execute:

```
python main.py
```
## Melhorias Implementadas

- Implementação de persistência de dados com SQLite
- Estruturação do banco de dados relacional
- Aplicação do padrão Repository para separação da camada de dados
- Separação clara entre Models, Repositories e Services
- Implementação de regras de negócio para empréstimos
- Tratamento de exceções e erros controlados
- Refatoração para melhorar organização e legibilidade
- Estrutura preparada para futura transformação em API REST

## Próximos Passos

- Transformar o sistema em uma API REST utilizando FastAPI
- Implementar validação com Pydantic
- Adicionar autenticação
- Criar interface web
- Implementar testes automatizados


# 👨‍💻 Desenvolvido por Guilherme Monteiro </>
