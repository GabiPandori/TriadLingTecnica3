from model.LivroMensalModel import LivroMensalModel

class LivroDao:
    livros = {
        1: {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "mes": 1},
        2: {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "mes": 2},
        3: {"titulo": "A Metamorfose", "autor": "Franz Kafka", "mes": 3}
    }

    @staticmethod
    def obterLivro(mes):
        for livro in LivroDao.livros.values():
            if str(livro.get("mes")) == str(mes):
                return livro
        return None
