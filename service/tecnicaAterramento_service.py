from repository.tecnicaAterramento_repository import TecnicaAterramentoRepository

class TecnicaAterramentoService:
    def __init__(self):
        self.tecnica_repo = TecnicaAterramentoRepository()

    def obterTecnica(self, idTecnica):
        if idTecnica <= 0:
            raise ValueError("ID da técnica inválido.")
        tecnica = self.tecnica_repo.obterTecnica(idTecnica)
        if not tecnica:
            raise ValueError("Técnica de aterramento não encontrada.")
        return tecnica

    def listarTecnicas(self):
        return self.tecnica_repo.listarTecnicas()
