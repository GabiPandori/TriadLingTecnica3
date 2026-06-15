from flask import Flask, Blueprint, request, jsonify
from model.UsuarioModel import UsuarioModel
from dao.UsuarioDao import UsuarioDao
usuario_bp = Blueprint('usuario', __name__)
usuario_dao = UsuarioDao()

#criar um usuario
@usuario_bp.route('', methods=['POST'])
def criarUsuario():
    dados = request.get_json()
    usuario = usuario_dao.criarUsuario(dados)
    return jsonify({"message": "Usuário criado com sucesso!", "dados": usuario}), 201

#mostar um usuario especifico
@usuario_bp.route('/<int:idUsuario>', methods=['GET'])
def obterUsuario(idUsuario):
    usuario = usuario_dao.obterUsuario(idUsuario)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"message": "Usuário não encontrado!"}), 404

#atualizar um usuario
@usuario_bp.route('/<int:idUsuario>', methods=['PUT'])
def atualizarUsuario(idUsuario):
    dados = request.get_json()
    usuario = usuario_dao.atualizarUsuario(idUsuario, dados)
    if usuario:
        return jsonify({"message": "Usuário atualizado com sucesso!", "dados": usuario}), 200
    else:
        return jsonify({"message": "Usuário não encontrado!"}), 404
    
#deletar um usuario
@usuario_bp.route('/<int:idUsuario>', methods=['DELETE'])
def excluirUsuario(idUsuario):
    sucesso = usuario_dao.excluirUsuario(idUsuario)
    if sucesso:
        return jsonify({"message": "Usuário excluído com sucesso!"}), 200
    else:
        return jsonify({"message": "Usuário não encontrado!"}), 404
