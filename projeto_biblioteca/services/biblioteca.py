from projeto_biblioteca.models.livro import Livro
from projeto_biblioteca.models.usuario import Usuario
import json
import os
from projeto_biblioteca.repositories.biblioteca_repository import BibliotecaRepository

class Biblioteca():
    """
        Classe responsável por gerenciar o sistema da biblioteca.

    Atributos:
        livros (list): Lista de objetos Livro cadastrados.
        usuarios (list): Lista de objetos Usuario cadastrados.
        ids_livros (int): Contador automático para IDs de livros.
        ids_usuarios (int): Contador automático para IDs de usuários.

    Métodos:
        adicionar_livro: Cadastra um novo livro.
        cadastrar_usuario: Cadastra um novo usuário.
        emprestar_livro: Realiza o empréstimo de um livro.
        devolver_livro: Registra a devolução de um livro.
        listar_livros: Exibe todos os livros cadastrados.
        listar_usuarios: Exibe todos os usuários cadastrados.
    """
    def __init__(self):
        self.repository = BibliotecaRepository()

# >>>>>>>>>>>>

#   CADASTRO

# <<<<<<<<<<<<

    def adicionar_livro(self, titulo, autor):
        self.repository.adicionar_livro(titulo, autor)
        print("O livro foi cadastrado com sucesso!")

    def cadastrar_usuario(self, nome): 
        self.repository.adicionar_usuario(nome)
        print("Usuário cadastrado com sucesso!")
    
# >>>>>>>>>>>

#   BUSCA

# <<<<<<<<<<<

    def buscar_livro_por_id(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None
    

    def buscar_usuario_por_id(self, id): 
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

# >>>>>>>>>>>>>>>>>

#   EMPRÉSTIMO

# <<<<<<<<<<<<<<<<<
       
    def emprestar_livro(self, usuario_id, livro_id):
        livro = self.repository.buscar_livro_por_id(livro_id)
        usuario = self.repository.buscar_usuario_por_id(usuario_id)

        if usuario is None:
            print("Usuário não encontrado.")
            return

        if livro is None:
            print("Livro não encontrado.")
            return

        if livro[3] == 1:
            print("Este livro ja foi emprestado.")
            return
        
        self.repository.registrar_emprestimo(usuario_id, livro_id)
        self.repository.atualizar_status_livro(livro_id, 1)
        
        print("Livro emprestado com sucesso!")

# <<<<<<<<<<<<<

#   DEVOLUÇÃO

# >>>>>>>>>>>>>

    def devolver_livro(self, usuario_id, livro_id):
        self.repository.remover_emprestimo(usuario_id, livro_id)
        self.repository.atualizar_status_livro(livro_id, 0)
        livro = self.repository.buscar_livro_por_id()
        emprestado = self.repository.verificar_emprestimo(usuario_id, livro_id)
        
        if emprestado is None:
            print("Esse usuário não possui esse livro.")
            return
        
        if livro is None:
            print("Livro não encontrado.")
            return
        
        if livro[3] == 0:
            print("O livro ja está disponivel.")

        print("Livro devolvido com sucesso!")
# <<<<<<<<<<<<<<<<<<<

#   LISTAGEM

# >>>>>>>>>>>>>>>>>>>

    def listar_livros(self):
        print("\n==== LISTA DE LIVROS ====")

        livros = self.repository.listar_livros()

        if not livros:
            print("Nenhum livro foi cadastrado.")
            return
        for livro in livros:
            id, titulo, autor, emprestado = livro
            if emprestado == 0:
                status = "Disponivel."
            else:
                status = "Emprestado."
            print(f"ID: {id}")
            print(f"Titulo: {titulo}")
            print(f"Autor: {autor}")
            print(f"Status: {status}")
            print("-==" * 8)



    def listar_usuarios(self):
        print("\n==== LISTA DE USUÁRIOS ====")
        usuarios = self.repository.listar_usuario()

        if not usuarios:
            print("Nenhum usuário foi cadastrado.")
            return
        
        for usuario in usuarios:
            id, nome = usuario
            print(f"ID: {id}")
            print(f"Nome: {nome}")
            print("-==" * 8)

