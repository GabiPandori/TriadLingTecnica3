from dao.LivroDao import LivroDao

class LivroRepository:
    def obterLivro(self, mes):
        return LivroDao.obterLivro(mes)
