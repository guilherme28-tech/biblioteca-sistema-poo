from projeto_biblioteca.services.biblioteca import Biblioteca
from time import sleep
from projeto_biblioteca.database import criar_tabelas

criar_tabelas()




def menu():
    sleep(0.75)
    print("\n ===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Adicionar livros")
    print("2 - Adicionar usuários")
    print("3 - Emprestar livros")
    print("4 - Devolver livros")
    print("5 - Listar livros")
    print("6 - Listar usuários")
    print("0 - Sair")
    sleep(0.5)


def main():
    
    biblioteca = Biblioteca()
    while True:

        menu()
        try:
            opção = int(input("Escolha uma opção: "))

        except ValueError:
            print("O valor da opção precisa ser um número inteiro.")

        if opção == 1:
            titulo = input("Titulo: ").title().strip()
            autor = input("Autor: ").title().strip()
            if not titulo or not autor:
                print("Os campos não podem estar vazios.")
            biblioteca.adicionar_livro(titulo, autor)

        elif opção == 2:
            nome = input("Nome do usuário: ").title().strip()
            if not nome:
                print("O campo não pode estar vazio.")
            biblioteca.cadastrar_usuario(nome)

        elif opção == 3:
            try:
                usuario_id = int(input("ID do usuário: "))
                livro_id = int(input("ID do livro: "))
            except ValueError:
                print("ERRO! os IDs devem ser números inteiros.")
                return
            biblioteca.emprestar_livro(usuario_id, livro_id)

        elif opção == 4:
            try:
                usuario_id = int(input("ID do usuário: "))
                livro_id = int(input("ID do livro: "))
            except ValueError:
                print("ERRO! os IDs devem ser números inteiros.")
                return
            biblioteca.devolver_livro(usuario_id, livro_id)

        elif opção == 5:
            biblioteca.listar_livros()

        elif opção == 6:
            biblioteca.listar_usuarios()

        elif opção == 0:
            print("Encerrando...")
            break

        else:
            print(f"a opção {opção} não existe. Tente novamente.")


if __name__ == "__main__":
    main()
        