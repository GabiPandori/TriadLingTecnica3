from dao.EventoDao import EventoDao

class EventoRepository:
    def obterEventos(self):
        return EventoDao.obterEventos()

    def mostrarDetalhesEvento(self, idEvento):
        return EventoDao.mostrarDetalhesEvento(idEvento)
