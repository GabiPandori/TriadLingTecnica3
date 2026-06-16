from flask import Blueprint, request, jsonify
from model.FraseDiariaModel import FraseDiariaModel
from dao.FraseDiariaDao import FraseDiariaDao

frase_bp = Blueprint('frase', __name__)
frase_dao = FraseDiariaDao()

@frase_bp.route('/<string:data>', methods=['GET'])
def obterFrase(data):
    frase = frase_dao.obterFrase(data)
    if frase:
        return jsonify({"message": "Frase encontrada!", "dados": frase}), 200
    return jsonify({"message": "Frase não encontrada!"}), 404

@frase_bp.route('', methods=['GET'])
def listarFrases():
    frases = frase_dao.listarFrases()
    return jsonify({"message": "Frases listadas!", "dados": frases}), 200
