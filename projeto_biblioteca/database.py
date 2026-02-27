import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        emprestado INTEGER NOT NULL DEFAULT 0
)
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        usuario_id INTEGER,
        FOREIGN KEY (livro_id) REFERENCES livro(id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")
    
    conn.commit()
    conn.close()