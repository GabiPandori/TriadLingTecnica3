from repository.frase_repository import FraseRepository

class FraseDiariaService:
    def __init__(self):
        self.frase_repo = FraseRepository()

    def obterFrase(self, data):
        frase = self.frase_repo.obterFrase(data)
        if not frase:
            raise ValueError("Frase não encontrada.")
        return frase

    def listarFrases(self):
        return self.frase_repo.listarFrases()
