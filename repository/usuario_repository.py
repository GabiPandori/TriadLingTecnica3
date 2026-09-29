from dao.UsuarioDao import UsuarioDao

class UsuarioRepository:
    def obterUsuario(self, usuario_id):
        return UsuarioDao.obterUsuario(usuario_id)

    def salvar(self, dados):
        return UsuarioDao.criarUsuario(dados)

    def atualizarUsuario(self, usuario_id, dados):
        return UsuarioDao.atualizarUsuario(usuario_id, dados)

    def excluirUsuario(self, usuario_id):
        return UsuarioDao.excluirUsuario(usuario_id)

    def email_ja_cadastrado(self, email):
        for usuario in UsuarioDao.usuarios.values():
            if usuario["email"] == email:
                return True
        return False
