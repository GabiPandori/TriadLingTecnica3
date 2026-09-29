from repository.diario_repository import DiarioRepository

class DiarioService:
    def __init__(self):
        self.diario_repo = DiarioRepository()

    def criarRelato(self, dados):
        if not dados or not dados.get('texto'):
            raise ValueError("Texto do relato é obrigatório.")
        return self.diario_repo.salvar(dados)

    def obterRelato(self, idDiario):
        if idDiario <= 0:
            raise ValueError("ID do relato inválido.")
        relato = self.diario_repo.obterRelato(idDiario)
        if not relato:
            raise ValueError("Relato não encontrado.")
        return relato

    def listarRelatos(self):
        return self.diario_repo.listarRelatos()

    def deletarRelato(self, idDiario):
        if not self.diario_repo.obterRelato(idDiario):
            raise ValueError("Relato não encontrado.")
        self.diario_repo.deletarRelato(idDiario)

    def atualizarRelato(self, idDiario, texto):
        if not texto:
            raise ValueError("Texto do relato é obrigatório.")
        relato = self.diario_repo.atualizarRelato(idDiario, texto)
        if not relato:
            raise ValueError("Relato não encontrado.")
        return relato
