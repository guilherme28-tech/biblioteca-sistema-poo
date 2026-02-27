class Usuario():
    """
    Representa um usuário da biblioteca.

    Atributos:
        id (int): Identificador único do usuário.
        nome (str): Nome do usuário.
        livros_emprestados (list): Lista de livros atualmente emprestados pra esse usuário.
    """
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.livros_emprestados = []
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "livros_emprestados": [livro.id for livro in self.livros_emprestados]
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["nome"]
        )