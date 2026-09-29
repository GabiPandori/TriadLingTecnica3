from model.UsuarioModel import UsuarioModel

class UsuarioDao:
    usuarios = {
        1: {"idUsuario": 1, "nome": "Gabi", "email": "gabi@gmail.com", "dataNasc": "2009-03-31", "genero": "Feminino", "telefone": "1234567890", "senha": "password123"},
        2: {"idUsuario": 2, "nome": "Amanda", "email": "amanda@gmail.com", "dataNasc": "2008-08-02", "genero": "Masculino", "telefone": "0987654321", "senha": "password456"}
    }

    @staticmethod
    def criarUsuario(dados):
        novo_id = max(UsuarioDao.usuarios.keys()) + 1
        usuario = UsuarioModel(
            idUsuario=novo_id,
            nome=dados['nome'],
            email=dados['email'],
            dataNasc=dados['dataNasc'],
            genero=dados['genero'],
            telefone=dados['telefone'],
            senha=dados['senha']
        )
        UsuarioDao.usuarios[novo_id] = usuario.__dict__
        return UsuarioDao.usuarios[novo_id]

    @staticmethod
    def obterUsuario(idUsuario):
        return UsuarioDao.usuarios.get(idUsuario)

    @staticmethod
    def atualizarUsuario(idUsuario, dados):
        if idUsuario in UsuarioDao.usuarios:
            usuario = UsuarioDao.usuarios[idUsuario]
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            usuario['dataNasc'] = dados.get('dataNasc', usuario['dataNasc'])
            usuario['genero'] = dados.get('genero', usuario['genero'])
            usuario['telefone'] = dados.get('telefone', usuario['telefone'])
            usuario['senha'] = dados.get('senha', usuario['senha'])
            return usuario
        return None

    @staticmethod
    def excluirUsuario(idUsuario):
        if idUsuario in UsuarioDao.usuarios:
            del UsuarioDao.usuarios[idUsuario]
            return True
        return False
