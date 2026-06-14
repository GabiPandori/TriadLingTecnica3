from flask import Flask, Blueprint, request, jsonify
from model.EventoModel import EventoModel
from dao.EventoDao import EventoDao
evento_bp = Blueprint(__name__, 'evento')
evento_dao = EventoDao()

@evento_bp.route('', methods=['GET'])
def obterEventos():
    evento = evento_dao.obterEventos()
    return jsonify({"eventos": evento}), 200

@evento_bp.route('/<int:idEvento>', methods=['GET'])
def mostrarDetalhesEvento(idEvento):
    evento = evento_dao.mostrarDetalhesEvento(idEvento)
    if evento:
        return jsonify({"evento": evento}), 200
    return jsonify({"message": "Evento não encontrado!"}), 404