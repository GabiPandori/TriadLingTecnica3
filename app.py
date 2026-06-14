from flask import Flask
from routes.diario_bp import diario_bp

app = Flask(__name__)
app.register_blueprint(diario_bp, url_prefix='/api/diario')

if __name__ == '__main__':
    app.run(debug=True)