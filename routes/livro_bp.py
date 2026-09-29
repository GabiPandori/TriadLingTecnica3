from flask import Blueprint, request, jsonify
from service.livro_service import LivroService

livro_bp = Blueprint('livro', __name__)
livro_service = LivroService()

@livro_bp.route('', methods=['GET'])
def obterLivro():
    try:
        livro = livro_service.obterLivro(request.args.get('mes'))
        return jsonify(livro), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
