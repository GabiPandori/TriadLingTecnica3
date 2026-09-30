from flask import Blueprint, request, jsonify
from service.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__)
usuario_service = UsuarioService()

@usuario_bp.route('', methods=['POST'])
def criarUsuario():
    dados = request.get_json() or {}
    try:
        usuario = usuario_service.criarUsuario(dados)
        return jsonify({"message": "Usuário criado com sucesso!", "dados": usuario}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@usuario_bp.route('/<int:idUsuario>', methods=['GET'])
def obterUsuario(idUsuario):
    try:
        usuario = usuario_service.obterUsuario(idUsuario)
        return jsonify(usuario), 200    
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@usuario_bp.route('/<int:idUsuario>', methods=['PUT'])
def atualizarUsuario(idUsuario):
    dados = request.get_json() or {}
    try:
        usuario = usuario_service.atualizarUsuario(idUsuario, dados)
        return jsonify({"message": "Usuário atualizado com sucesso!", "dados": usuario}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@usuario_bp.route('/<int:idUsuario>', methods=['DELETE'])
def excluirUsuario(idUsuario):
    try:
        usuario_service.excluirUsuario(idUsuario)
        return jsonify({"message": "Usuário excluído com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
