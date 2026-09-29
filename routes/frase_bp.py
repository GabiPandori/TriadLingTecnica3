from flask import Blueprint, jsonify
from service.fraseDiaria_service import FraseDiariaService

frase_bp = Blueprint('frase', __name__)
frase_service = FraseDiariaService()

@frase_bp.route('/<string:data>', methods=['GET'])
def obterFrase(data):
    try:
        frase = frase_service.obterFrase(data)
        return jsonify({"message": "Frase encontrada!", "dados": frase}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@frase_bp.route('', methods=['GET'])
def listarFrases():
    return jsonify({"message": "Frases listadas!", "dados": frase_service.listarFrases()}), 200
