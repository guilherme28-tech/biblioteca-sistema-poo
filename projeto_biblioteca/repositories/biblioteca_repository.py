from projeto_biblioteca.database import conectar

class BibliotecaRepository:

    def adicionar_livro(self, titulo, autor):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO livros (titulo, autor, emprestado) VALUES (?, ?, 0)",
            (titulo, autor)
        )

        conn.commit()
        conn.close()

    def listar_livros(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, titulo, autor, emprestado FROM livros"
)
        livros = cursor.fetchall()

        conn.close()
        return livros

    def adicionar_usuario(self, nome):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome) VALUES (?)",
            (nome,)
)
        conn.commit()
        conn.close()
 
    def listar_usuario(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome FROM usuarios")
        usuarios = cursor.fetchall()

        conn.close()
        return usuarios
    
    def buscar_livro_por_id(self, livro_id):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, titulo, autor, emprestado FROM livros WHERE id = ?",
                        (livro_id,)
)
        
        livro = cursor.fetchone()
        conn.close()

        return livro
    
    def buscar_usuario_por_id(self, usuario_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome FROM usuarios WHERE id = ?",
                       (usuario_id)
)
        usuario = cursor.fetchone()
        conn.close()
        
        return usuario 

    def registrar_emprestimo(self, usuario_id, livro_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO emprestado (livro_id, usuario_id) VALUES (?, ?)",
            (livro_id, usuario_id)
)
        conn.commit()
        conn.close()

    def remover_emprestimo(self, usuario_id, livro_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM emprestado WHERE livro_id = ? AND usuario_id = ?",
            (livro_id, usuario_id)
)
        conn.commit()
        conn.close()

    def atualizar_status_livro(self, livro_id, emprestado):
        
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute(
            "UPDATE livros SET emprestado = ? WHERE id = ?",
            (emprestado, livro_id)
)
        print(cursor.rowcount)
        conn.commit()
        conn.close()

    def verificar_emprestimo(self, usuario_id, livro_id):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM WHERE emprestado usuario_id = ? AND livro_id = ?",
            (usuario_id, livro_id)
)
        emprestimo = cursor.fetchone()

        conn.close()
        return emprestimo
