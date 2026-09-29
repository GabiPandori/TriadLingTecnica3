from flask import Blueprint, jsonify
from service.evento_service import EventoService

evento_bp = Blueprint('evento', __name__)
evento_service = EventoService()

@evento_bp.route('', methods=['GET'])
def obterEventos():
    return jsonify({"eventos": evento_service.obterEventos()}), 200

@evento_bp.route('/<int:idEvento>', methods=['GET'])
def mostrarDetalhesEvento(idEvento):
    try:
        evento = evento_service.mostrarDetalhesEvento(idEvento)
        return jsonify({"evento": evento}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
