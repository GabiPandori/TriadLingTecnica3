from dao.DiarioDao import DiarioDao

class DiarioRepository:
    def obterRelato(self, idDiario):
        return DiarioDao.obterRelato(idDiario)

    def salvar(self, dados):
        return DiarioDao.criarRelato(dados)

    def listarRelatos(self):
        return DiarioDao.listarRelatos()

    def deletarRelato(self, idDiario):
        return DiarioDao.deletarRelato(idDiario)

    def atualizarRelato(self, idDiario, texto):
        return DiarioDao.atualizarRelato(idDiario, texto)
