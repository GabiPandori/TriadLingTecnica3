from flask import Blueprint, request, jsonify
from service.profissional_service import ProfissionalService

profissional_bp = Blueprint('profissional', __name__)
profissional_service = ProfissionalService()

@profissional_bp.route('', methods=['POST'])
def criarProfissional():
    dados = request.get_json() or {}
    try:
        profissional = profissional_service.criarProfissional(dados)
        return jsonify({"message": "Profissional criado com sucesso!", "dados": profissional}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@profissional_bp.route('/<int:idProfissional>', methods=['GET'])
def obterProfissional(idProfissional):
    try:
        profissional = profissional_service.obterProfissional(idProfissional)
        return jsonify(profissional), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@profissional_bp.route('/<int:idProfissional>', methods=['PUT'])
def atualizarProfissional(idProfissional):
    dados = request.get_json() or {}
    try:
        profissional = profissional_service.atualizarProfissional(idProfissional, dados)
        return jsonify({"message": "Profissional atualizado com sucesso!", "dados": profissional}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@profissional_bp.route('/<int:idProfissional>', methods=['DELETE'])
def excluirProfissional(idProfissional):
    try:
        profissional_service.excluirProfissional(idProfissional)
        return jsonify({"message": "Profissional excluído com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
