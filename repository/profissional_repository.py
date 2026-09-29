from dao.ProfissionalDao import ProfissionalDao

class ProfissionalRepository:
    def salvar(self, dados):
        return ProfissionalDao.criarProfissional(dados)

    def obterProfissional(self, idProfissional):
        return ProfissionalDao.obterProfissional(idProfissional)

    def atualizarProfissional(self, idProfissional, dados):
        return ProfissionalDao.atualizarProfissional(idProfissional, dados)

    def excluirProfissional(self, idProfissional):
        return ProfissionalDao.excluirProfissional(idProfissional)
