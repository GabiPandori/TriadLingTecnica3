from repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def criarUsuario(self, dados):
        campos = ['nome', 'email', 'dataNasc', 'genero', 'telefone', 'senha']
        if not dados or any(not dados.get(campo) for campo in campos):
            raise ValueError("Todos os campos do usuário são obrigatórios.")
        if "@" not in dados.get('email', ''):
            raise ValueError("Formato de e-mail inválido.")
        if self.usuario_repo.email_ja_cadastrado(dados['email']):
            raise ValueError("Este e-mail já está em uso por outro usuário.")
        return self.usuario_repo.salvar(dados)

    def obterUsuario(self, idUsuario):
        if idUsuario <= 0:
            raise ValueError("ID de usuário inválido.")
        usuario = self.usuario_repo.obterUsuario(idUsuario)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        return usuario

    def atualizarUsuario(self, idUsuario, dados):
        usuario = self.usuario_repo.atualizarUsuario(idUsuario, dados)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        return usuario

    def excluirUsuario(self, idUsuario):
        if not self.usuario_repo.excluirUsuario(idUsuario):
            raise ValueError("Usuário não encontrado.")
