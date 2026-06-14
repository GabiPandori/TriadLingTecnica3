from model.LivroMensalModel import LivroMensalModel
class LivroDao:
    def __init__(self):
        self.livros = {
            1: {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
            2: {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes"},
            3: {"titulo": "A Metamorfose", "autor": "Franz Kafka"}
        }

    def obterLivro(self, mes):
        for livro in self.livros.values():
            if livro.get("mes") == mes:
                return livro
        return None
    