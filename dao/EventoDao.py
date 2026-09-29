from model.EventoModel import EventoModel

class EventoDao:
    eventos = {
        1: {"idEvento": 1, "tema": "Conferência Plenituide", "data": "2026-09-12"},
        2: {"idEvento": 2, "tema": "Congresso de felicidade", "data": "2026-11-14"},
        3: {"idEvento": 3, "tema": "Inteligência Emocional", "data": "2026-08-18"}
    }

    @staticmethod
    def obterEventos():
        return list(EventoDao.eventos.values())

    @staticmethod
    def mostrarDetalhesEvento(idEvento):
        return EventoDao.eventos.get(idEvento)
