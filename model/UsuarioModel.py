class UsuarioModel:
    def __init__(self, idUsuario=None, nome=None, telefone=None, dataNasc=None, genero=None, email=None, senha=None):
        self.idUsuario = idUsuario
        self.nome = nome
        self.telefone = telefone
        self.dataNasc = dataNasc
        self.genero = genero
        self.email = email
        self.senha = senha