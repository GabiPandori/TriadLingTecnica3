from model.DiarioModel import DiarioModel

class DiarioDao:
    relatos = {
        1: {"idDiario": 1, "texto": "Hoje foi um dia incrível!", "data": "2026-06-01"},
        2: {"idDiario": 2, "texto": "Aprendi algo novo hoje.", "data": "2026-06-02"},
        3: {"idDiario": 3, "texto": "Estou me sentindo grato.", "data": "2026-06-03"}
    }

    @staticmethod
    def obterRelato(idDiario):
        return DiarioDao.relatos.get(idDiario)

    @staticmethod
    def criarRelato(dados):
        idDiario = max(DiarioDao.relatos.keys()) + 1
        relato = DiarioModel(idDiario=idDiario, texto=dados.get('texto'), data="hoje")
        DiarioDao.relatos[idDiario] = {
            "idDiario": idDiario,
            "texto": relato.texto,
            "data": relato.data
        }
        return DiarioDao.relatos[idDiario]

    @staticmethod
    def listarRelatos():
        return list(DiarioDao.relatos.values())

    @staticmethod
    def deletarRelato(idDiario):
        return DiarioDao.relatos.pop(idDiario, None)

    @staticmethod
    def atualizarRelato(idDiario, texto):
        if idDiario in DiarioDao.relatos:
            DiarioDao.relatos[idDiario]['texto'] = texto
            return DiarioDao.relatos[idDiario]
        return None
