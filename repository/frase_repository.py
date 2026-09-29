from dao.FraseDiariaDao import FraseDiariaDao

class FraseRepository:
    def obterFrase(self, data):
        return FraseDiariaDao.obterFrase(data)

    def listarFrases(self):
        return FraseDiariaDao.listarFrases()
