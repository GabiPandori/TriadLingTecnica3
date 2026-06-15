from model.UsuarioModel import UsuarioModel
class UsuarioDao:
    def __init__(self):
        self.usuarios = {
            1: {"idUsuario": 1, "nome": "Gabi", "email": "gabi@gmail.com", "dataNasc": "2009-03-31", "genero": "Feminino", "telefone": "1234567890", "senha": "password123"},
            2: {"idUsuario": 2, "nome": "Amanda", "email": "amanda@gmail.com", "dataNasc": "2008-08-02", "genero": "Masculino", "telefone": "0987654321", "senha": "password456"}
        }

    def criarUsuario(self, dados):
        novo_id = max(self.usuarios.keys()) + 1
        usuario = UsuarioModel(
            idUsuario=novo_id,
            nome=dados['nome'],
            email=dados['email'],
            dataNasc=dados['dataNasc'],
            genero=dados['genero'],
            telefone=dados['telefone'],
            senha=dados['senha']
        )
        self.usuarios[novo_id] = usuario.__dict__
        return self.usuarios[novo_id]
    
    def obterUsuario(self, idUsuario):
        return self.usuarios.get(idUsuario)
    
    def atualizarUsuario(self, idUsuario, dados):
        if idUsuario in self.usuarios:
            usuario = self.usuarios[idUsuario]
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            usuario['dataNasc'] = dados.get('dataNasc', usuario['dataNasc'])
            usuario['genero'] = dados.get('genero', usuario['genero'])
            usuario['telefone'] = dados.get('telefone', usuario['telefone'])
            usuario['senha'] = dados.get('senha', usuario['senha'])
            return usuario
        return None
    
    def excluirUsuario(self, idUsuario):
        if idUsuario in self.usuarios:
            del self.usuarios[idUsuario]
            return True
        return False