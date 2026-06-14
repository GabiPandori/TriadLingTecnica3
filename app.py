from flask import Flask
from routes.diario_bp import diario_bp
from routes.evento_bp import evento_bp
app = Flask(__name__)
app.register_blueprint(diario_bp, url_prefix='/api/diario')
app.register_blueprint(evento_bp, url_prefix='/api/evento')

if __name__ == '__main__':
    app.run(debug=True)