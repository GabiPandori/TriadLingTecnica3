from model.FraseDiariaModel import FraseDiariaModel

class FraseDiariaDao:
    fraseDiarias = {
        1: {"frase": "A vida é bela!", "data": "2026-06-01"},
        2: {"frase": "Cada dia é uma nova oportunidade.", "data": "2026-06-02"},
        3: {"frase": "Sorria para a vida!", "data": "2026-06-03"}
    }

    @staticmethod
    def obterFrase(data):
        for frase_info in FraseDiariaDao.fraseDiarias.values():
            if frase_info["data"] == data:
                return frase_info
        return None

    @staticmethod
    def listarFrases():
        return list(FraseDiariaDao.fraseDiarias.values())
