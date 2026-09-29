from model.ProfissionalModel import ProfissionalModel

class ProfissionalDao:
    profissionais = {
        1: {"idProfissional": 1, "nome": "Alice", "telefone": "11988002297", "dataNasc": "1981-10-12", "genero": "Feminino", "documentoCip": "15el554", "email": "alicesantos@gmail.com", "senha": "47190"},
        2: {"idProfissional": 2, "nome": "Carlos", "telefone": "11988002207", "dataNasc": "1979-11-29", "genero": "Masculino", "documentoCip": "17334sp", "email": "carlosalberto@gmail.com", "senha": "29182"}
    }

    @staticmethod
    def criarProfissional(dados):
        novo_id = max(ProfissionalDao.profissionais.keys()) + 1
        profissional = ProfissionalModel(
            idProfissional=novo_id,
            nome=dados['nome'],
            telefone=dados['telefone'],
            dataNasc=dados['dataNasc'],
            genero=dados['genero'],
            documentoCip=dados['documentoCip'],
            email=dados['email'],
            senha=dados['senha']
        )
        ProfissionalDao.profissionais[novo_id] = profissional.__dict__
        return ProfissionalDao.profissionais[novo_id]

    @staticmethod
    def obterProfissional(idProfissional):
        return ProfissionalDao.profissionais.get(idProfissional)

    @staticmethod
    def atualizarProfissional(idProfissional, dados):
        if idProfissional in ProfissionalDao.profissionais:
            profissional = ProfissionalDao.profissionais[idProfissional]
            profissional['nome'] = dados.get('nome', profissional['nome'])
            profissional['email'] = dados.get('email', profissional['email'])
            profissional['dataNasc'] = dados.get('dataNasc', profissional['dataNasc'])
            profissional['genero'] = dados.get('genero', profissional['genero'])
            profissional['telefone'] = dados.get('telefone', profissional['telefone'])
            profissional['senha'] = dados.get('senha', profissional['senha'])
            profissional['documentoCip'] = dados.get('documentoCip', profissional['documentoCip'])
            return profissional
        return None

    @staticmethod
    def excluirProfissional(idProfissional):
        if idProfissional in ProfissionalDao.profissionais:
            del ProfissionalDao.profissionais[idProfissional]
            return True
        return False
