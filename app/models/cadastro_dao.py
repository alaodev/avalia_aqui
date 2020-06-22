SQL_VERIFICA_USUARIO = 'SELECT usuario FROM usuario WHERE usuario = %s'
SQL_CRIA_USUARIO = 'INSERT INTO usuario (usuario, senha) VALUES (%s, %s)'

class CadastroDao:
    def __init__(self, db):
        self.db = db

    def verifica_usuario(self, usuario):
        cur = self.db.connection.cursor()
        cur.execute(SQL_VERIFICA_USUARIO, (usuario, ))
        usuario_db = cur.fetchone()

        return usuario_db

    def cria_usuario(self, usuario, senha):
        cur = self.db.connection.cursor()
        cur.execute(SQL_CRIA_USUARIO, (usuario, senha, ))
        self.db.connection.commit()

    def valida_login(self, usuario):
        cur = self.db.connection.cursor()
        cur.execute(SQL_VALIDA_LOGIN, (usuario, ))
        usuario_db = cur.fetchone()

        return usuario_db