class Livro():
    """   
    Representa um livro dentro da biblioteca.

    Atributos:
        id (int): Identificador único do livro.
        titulo (str): Título do livro.
        autor (str): Autor do livro.
        disponivel (bool): Indica se o livro está disponível para empréstimo.
    """
    def __init__(self, id, titulo, autor, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponivel": self.disponivel
        }
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["titulo"],
            dados["autor"],
            dados["disponivel"]
        )