from flask import Flask, Blueprint, request, jsonify
from model.DiarioModel import DiarioModel
from dao.DiarioDao import DiarioDao
diario_bp = Blueprint('diario', __name__)
diario_dao = DiarioDao()

@diario_bp.route('', methods=['POST'])
def criarRelato():
    dados = request.get_json()
    relato = diario_dao.criarRelato(dados)
    return jsonify({"message": "Relato criado com sucesso!", "dados": relato}), 201

@diario_bp.route('/<int:idDiario>', methods=['GET'])
def obterRelato(idDiario):
    relato = diario_dao.obterRelato(idDiario)
    if relato:
        return jsonify({"relato": relato}), 200
    return jsonify({"message": "Relato não encontrado!"}), 404

@diario_bp.route('', methods=['GET'])
def listarRelatos():
    relatos = diario_dao.listarRelatos()
    return jsonify({"relatos": relatos}), 200

@diario_bp.route('/<int:idDiario>', methods=['DELETE'])
def deletarRelato(idDiario):
    relato = diario_dao.obterRelato(idDiario)
    if relato:
        diario_dao.deletarRelato(idDiario)
        return jsonify({"message": "Relato deletado com sucesso!"}), 200
    return jsonify({"message": "Relato não encontrado!"}), 404

@diario_bp.route('/<int:idDiario>', methods=['PUT'])
def atualizarRelato(idDiario):
    relato = diario_dao.obterRelato(idDiario)
    if relato:
        dados = request.get_json()
        diario_dao.atualizarRelato(idDiario, dados.get('texto'))
        return jsonify({"message": "Relato atualizado com sucesso!"}), 200
    return jsonify({"message": "Relato não encontrado!"}), 404
