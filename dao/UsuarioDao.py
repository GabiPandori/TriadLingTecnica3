from model.UsuarioModel import UsuarioModel
class UsuarioDao:
    def __init__(self):
        self.usuarios = {
            1: {"idUsuario": 1, "nome": "Gabi", "email": "gabi@gmail.com", "dataNasc": "2009-03-31", "genero": "Feminino", "telefone": "1234567890", "senha": "password123"},
            2: {"idUsuario": 2, "nome": "Amanda", "email": "amanda@gmail.com", "dataNasc": "2008-08-02", "genero": "Masculino", "telefone": "0987654321", "senha": "password456"}
        }

    