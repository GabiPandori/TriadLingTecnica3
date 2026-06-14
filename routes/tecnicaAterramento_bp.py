from flask import Flask, Blueprint, request, jsonify
from model.TecnicaAterramentoModel import TecnicaAterramentoModel
from dao.TecnicaAterramentoDao import TecnicaAterramentoDao
tecnicaAterramento_bp = Blueprint('tecnicaAterramento_bp', __name__)
tecnicaAterramento_dao = TecnicaAterramentoDao()

@tecnicaAterramento_bp.route('/tecnicaAterramento/<int:idTecnica>', methods=['GET'])
def obterTecnica(idTecnica):
    tecnica = tecnicaAterramento_dao.obterTecnica(idTecnica)
    if tecnica:
        return jsonify(tecnica), 200
    else:
        return jsonify({"error": "Técnica de aterramento não encontrada."}), 404
    
@tecnicaAterramento_bp.route('/tecnicaAterramento', methods=['GET'])
def listarTecnicas():
    tecnicas = tecnicaAterramento_dao.listarTecnicas()
    return jsonify(tecnicas), 200