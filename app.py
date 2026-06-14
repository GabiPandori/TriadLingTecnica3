from flask import Flask
from routes.diario_bp import diario_bp
from routes.evento_bp import evento_bp
from routes.livro_bp import livro_bp
from routes.frase_bp import frase_bp

app = Flask(__name__)
app.register_blueprint(diario_bp, url_prefix='/api/diario')
app.register_blueprint(evento_bp, url_prefix='/api/evento')
app.register_blueprint(livro_bp, url_prefix='/api/livro')
app.register_blueprint(frase_bp, url_prefix='/api/frase')

if __name__ == '__main__':
    app.run(debug=True)