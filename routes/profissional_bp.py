# from flask import Flask, Blueprint, request, jsonify
# from model.ProfissionalModel import ProfissionalModel
# from dao.ProfissionalDao import ProfissionalDao
# profissional_bp = Blueprint('profissional', __name__)
# profissional_dao = ProfissionalDao()

# #criar um profissional
# @profissional_bp.route('', methods=['POST'])
# def criarProfissional():
#     dados = request.get_json()
#     profissional = profissional_dao.criarProfissional(dados)
#     return jsonify({"message": "Profissional criado com sucesso!", "dados": profissional}), 201

# #mostar um profissional especifico
# @profissional_bp.route('/<int:idProfissional>', methods=['GET'])
# def obterProfissional(idProfissional):
#     profissional = profissional_dao.obterProfissional(idProfissional)
#     if profissional:
#         return jsonify(profissional), 200
#     else:
#         return jsonify({"message": "Profissional não encontrado!"}), 404

# #atualizar um profissional
# @profissional_bp.route('/<int:idProfissional>', methods=['PUT'])
# def atualizarProfissional(idProfissional):
#     dados = request.get_json()
#     profissional = profissional_dao.atualizarProfissional(idProfissional, dados)
#     if profissional:
#         return jsonify({"message": "Profissional atualizado com sucesso!", "dados": profissional}), 200
#     else:
#         return jsonify({"message": "Profissional não encontrado!"}), 404

# #deletar um profissional
# @profissional_bp.route('/<int:idProfissional>', methods=['DELETE'])
# def excluirProfissional(idProfissional):
#     sucesso = profissional_dao.excluirProfissional(idProfissional)
#     if sucesso:
#         return jsonify({"message": "Profissional excluído com sucesso!"}), 200
#     else:
#         return jsonify({"message": "Profissional não encontrado!"}), 404
