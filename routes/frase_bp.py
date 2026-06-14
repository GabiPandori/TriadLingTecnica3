from flask import Flask, Blueprint, request, jsonify
from model.FraseDiariaModel import FrseDiariaModel
from dao.FraseDiariaDao import FraseDiariaDao
frase_bp = Blueprint('frase', __name__) 
frase_dao = FraseDiariaDao()

@frase_bp.route('/frase/<date:data>', methods=['GET'])
def obterFrase():
    idFraseDiaria = request.args.get('data')
    frase = frase_dao.obterFrase(data)
    if frase:
        return jsonify({"message": "Frase encontrada!", "dados": frase}), 200
    return jsonify({"message": "Frase não encontrada!"}), 404

@frase_bp.route('', methods=['GET'])
def listarFrases():
    frases = frase_dao.listarFrases()
    return jsonify({"message": "Frasess listadas!", "dados": frases}), 200