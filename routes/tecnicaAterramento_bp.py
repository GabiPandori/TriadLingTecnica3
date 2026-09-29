from flask import Blueprint, jsonify
from service.tecnicaAterramento_service import TecnicaAterramentoService

tecnicaAterramento_bp = Blueprint('tecnicaAterramento_bp', __name__)
tecnicaAterramento_service = TecnicaAterramentoService()

@tecnicaAterramento_bp.route('/<int:idTecnica>', methods=['GET'])
def obterTecnica(idTecnica):
    try:
        tecnica = tecnicaAterramento_service.obterTecnica(idTecnica)
        return jsonify(tecnica), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@tecnicaAterramento_bp.route('', methods=['GET'])
def listarTecnicas():
    return jsonify(tecnicaAterramento_service.listarTecnicas()), 200
