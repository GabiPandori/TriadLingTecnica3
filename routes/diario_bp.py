from flask import Blueprint, request, jsonify
from service.diario_service import DiarioService

diario_bp = Blueprint('diario', __name__)
diario_service = DiarioService()

@diario_bp.route('', methods=['POST'])
def criarRelato():
    dados = request.get_json() or {}
    try:
        relato = diario_service.criarRelato(dados)
        return jsonify({"message": "Relato criado com sucesso!", "dados": relato}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@diario_bp.route('/<int:idDiario>', methods=['GET'])
def obterRelato(idDiario):
    try:
        relato = diario_service.obterRelato(idDiario)
        return jsonify({"relato": relato}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@diario_bp.route('', methods=['GET'])
def listarRelatos():
    return jsonify({"relatos": diario_service.listarRelatos()}), 200

@diario_bp.route('/<int:idDiario>', methods=['DELETE'])
def deletarRelato(idDiario):
    try:
        diario_service.deletarRelato(idDiario)
        return jsonify({"message": "Relato deletado com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@diario_bp.route('/<int:idDiario>', methods=['PUT'])
def atualizarRelato(idDiario):
    dados = request.get_json() or {}
    try:
        diario_service.atualizarRelato(idDiario, dados.get('texto'))
        return jsonify({"message": "Relato atualizado com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
