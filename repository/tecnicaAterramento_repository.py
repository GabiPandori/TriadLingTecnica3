from dao.TecnicaAterramentoDao import TecnicaAterramentoDao

class TecnicaAterramentoRepository:
    def obterTecnica(self, idTecnica):
        return TecnicaAterramentoDao.obterTecnica(idTecnica)

    def listarTecnicas(self):
        return TecnicaAterramentoDao.listarTecnicas()
    