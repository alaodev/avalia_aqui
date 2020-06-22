SQL_VALIDA_LOGIN = 'SELECT * FROM usuario WHERE usuario = %s'
SQL_BUSCA_USUARIO_ID = 'SELECT * FROM usuario WHERE id_usuario = %s'

class LoginDao:
    def __init__(self, db):
        self.db = db

    def valida_login(self, usuario):
        cur = self.db.connection.cursor()
        cur.execute(SQL_VALIDA_LOGIN, (usuario, ))
        usuario_db = cur.fetchone()

        return usuario_db

    def busca_usuario_id(self, id_usuario):
        cur = self.db.connection.cursor()
        cur.execute(SQL_BUSCA_USUARIO_ID, (id_usuario, ))
        usuario_db = cur.fetchone()

        return usuario_db