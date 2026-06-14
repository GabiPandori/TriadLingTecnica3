from flask import Flask, Blueprint, request, jsonify
from model.LivroMensalModel import LivroMensalModel
from dao.LivroDao import LivroDao
livro_bp = Blueprint('livro', __name__)
livro_dao = LivroDao()

@livro_bp.route('', methods=['GET'])
def obterLivro():
    livro = livro_dao.obterLivro(request.args.get('mes'))
    if livro:
        return jsonify(livro), 200  
    else:
        return jsonify({"message": "Livro não encontrado para o mês especificado."}), 404