from repository.evento_repository import EventoRepository

class EventoService:
    def __init__(self):
        self.evento_repo = EventoRepository()

    def obterEventos(self):
        return self.evento_repo.obterEventos()

    def mostrarDetalhesEvento(self, idEvento):
        if idEvento <= 0:
            raise ValueError("ID do evento inválido.")
        evento = self.evento_repo.mostrarDetalhesEvento(idEvento)
        if not evento:
            raise ValueError("Evento não encontrado.")
        return evento
