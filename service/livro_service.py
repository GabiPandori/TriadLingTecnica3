from repository.livro_repository import LivroRepository

class LivroService:
    def __init__(self):
        self.livro_repo = LivroRepository()

    def obterLivro(self, mes):
        if not mes:
            raise ValueError("Mês é obrigatório.")
        livro = self.livro_repo.obterLivro(mes)
        if not livro:
            raise ValueError("Livro não encontrado para o mês especificado.")
        return livro
