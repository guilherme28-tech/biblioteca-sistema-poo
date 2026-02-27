# 📚 Sistema de Gerenciamento de Biblioteca

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Architecture](https://img.shields.io/badge/Architecture-Layered-blueviolet)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-green)
![Status](https://img.shields.io/badge/Status-Em%20Evolução-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)
![GitHub last commit](https://img.shields.io/github/last-commit/guilherme28-tech/biblioteca-sistema-poo)
![GitHub repo size](https://img.shields.io/github/repo-size/guilherme28-tech/biblioteca-sistema-poo)

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, com foco em arquitetura backend profissional, aplicação de **POO**, separação de camadas e regras de negócio reais.

O projeto simula um backend estruturado como em aplicações de mercado, com organização escalável e preparado para futura transformação em API REST.

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o propósito de aplicar e consolidar conhecimentos fundamentais de backend, como:

- Programação Orientada a Objetos
- Arquitetura em camadas
- Separação de responsabilidades
- Persistência relacional com SQLite
- Implementação do padrão Repository
- Regras de negócio reais
- Tratamento de exceções
- Estrutura escalável e organizada

---

# 🏗️ Arquitetura do Projeto

O sistema foi organizado pensando em como aplicações backend reais são estruturadas.  
Cada parte do projeto tem uma responsabilidade bem definida, o que facilita manutenção, evolução e entendimento do código.

A estrutura está dividida da seguinte forma:

- **Models** → Representam as entidades do sistema (Usuário, Livro).
- **Repositories** → Responsáveis por acessar e manipular os dados no banco SQLite.
- **Services** → Onde ficam as regras de negócio e validações do sistema.
- **Database** → Configuração e conexão com o banco de dados.
- **Main** → Ponto de entrada da aplicação.

Essa separação permite que:

- As regras de negócio não fiquem misturadas com o acesso ao banco.
- O sistema seja mais organizado e fácil de manter.
- Novas funcionalidades possam ser adicionadas com menor impacto no código existente.
- O projeto possa evoluir futuramente para uma API REST sem grandes mudanças estruturais. 

---

# ⚙️ Funcionalidades

## 👤 Usuários
- Cadastro de usuários  
- Listagem de usuários  

## 📖 Livros
- Cadastro de livros  
- Listagem de livros  
- Controle de disponibilidade  

## 🔄 Empréstimos
- Realização de empréstimo  
- Bloqueio de empréstimo de livro indisponível  
- Devolução de livro  
- Atualização automática do status do livro  

---

# 🛠️ Tecnologias Utilizadas

- Python 3.10+
- SQLite
- Padrão Repository
- Arquitetura em Camadas
- Git e GitHub

---

# 🚀 Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/guilherme28-tech/biblioteca-sistema-poo.git
```

## 2️⃣ Acessar a pasta do projeto

```bash
cd biblioteca-sistema-poo
```

## 3️⃣ Executar a aplicação

```bash
python main.py
```

---

# 📈 Melhorias Implementadas

- Implementação de persistência com SQLite  
- Estruturação de banco de dados relacional  
- Aplicação do padrão Repository  
- Separação entre Models, Repositories e Services  
- Implementação de regras de negócio reais  
- Tratamento de exceções e erros controlados  
- Refatoração para melhoria de organização e legibilidade  
- Estrutura preparada para futura transformação em API REST  

---

# Próximos Passos

- Transformar o sistema em API REST utilizando FastAPI  
- Implementar validação de dados com Pydantic  
- Adicionar autenticação  
- Criar testes automatizados com pytest  
- Containerizar com Docker  
- Desenvolver interface web  

---

# 👨‍💻 Desenvolvido por Guilherme Monteiro
