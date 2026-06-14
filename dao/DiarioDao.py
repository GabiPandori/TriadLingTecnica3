from model.DiarioModel import DiarioModel
class DiarioDao:
    def __init__(self):
        self.relatos = {
            1: {"idDiario": 1, "texto": "Hoje foi um dia incrível!", "data": "2026-06-01"},
            2: {"idDiario": 2, "texto": "Aprendi algo novo hoje.", "data": "2026-06-02"},
            3: {"idDiario": 3, "texto": "Estou me sentindo grato.", "data": "2026-06-03"}
        }

    def obterRelato(self, idDiario):
        return self.relatos.get(idDiario, None)
    
    def criarRelato(self, dados):
        idDiario = max(self.relatos.keys()) + 1
        relato = DiarioModel(idDiario=idDiario,texto=dados.get('texto'),data="hoje")
        self.relatos[idDiario] = {
            "idDiario": idDiario,
            "texto": relato.texto,
            "data":relato.data
        }
        return relato
    
    def listarRelatos(self):
        listaRelatos = list(self.relatos.values())
        return listaRelatos
    
    def deletarRelato(self, idDiario):
        return self.relatos.pop(idDiario, None)
    
    def atualizarRelato(self, idDiario, texto):
        if idDiario in self.relatos:
            self.relatos[idDiario]['texto'] = texto
            return self.relatos[idDiario]
        return None