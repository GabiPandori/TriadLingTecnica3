from repository.profissional_repository import ProfissionalRepository

class ProfissionalService:
    def __init__(self):
        self.profissional_repo = ProfissionalRepository()

    def criarProfissional(self, dados):
        campos = ['nome', 'telefone', 'dataNasc', 'genero', 'documentoCip', 'email', 'senha']
        if not dados or any(not dados.get(campo) for campo in campos):
            raise ValueError("Todos os campos do profissional são obrigatórios.")
        return self.profissional_repo.salvar(dados)

    def obterProfissional(self, idProfissional):
        if idProfissional <= 0:
            raise ValueError("ID do profissional inválido.")
        profissional = self.profissional_repo.obterProfissional(idProfissional)
        if not profissional:
            raise ValueError("Profissional não encontrado.")
        return profissional

    def atualizarProfissional(self, idProfissional, dados):
        profissional = self.profissional_repo.atualizarProfissional(idProfissional, dados)
        if not profissional:
            raise ValueError("Profissional não encontrado.")
        return profissional

    def excluirProfissional(self, idProfissional):
        if not self.profissional_repo.excluirProfissional(idProfissional):
            raise ValueError("Profissional não encontrado.")
