from flask import Flask
from routes.diario_bp import diario_bp
from routes.evento_bp import evento_bp
from routes.livro_bp import livro_bp
from routes.frase_bp import frase_bp
from routes.tecnicaAterramento_bp import tecnicaAterramento_bp
from routes.usuario_bp import usuario_bp
from routes.profissional_bp import profissional_bp

app = Flask(__name__)
app.register_blueprint(diario_bp, url_prefix='/api/diario')
app.register_blueprint(evento_bp, url_prefix='/api/evento')
app.register_blueprint(livro_bp, url_prefix='/api/livro')
app.register_blueprint(frase_bp, url_prefix='/api/frase')
app.register_blueprint(tecnicaAterramento_bp, url_prefix='/api/tecnicaAterramento')
app.register_blueprint(usuario_bp, url_prefix='/api/usuario')
app.register_blueprint(profissional_bp, url_prefix='/api/profissional')
if __name__ == '__main__':
    app.run(debug=True)