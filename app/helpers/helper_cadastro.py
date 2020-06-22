from app import mysql
from app.models.cadastro_dao import CadastroDao

def verifica_usuario(usuario): # True = Usuário existente. False = Usuário Inexistente.
    cadasto_dao = CadastroDao(mysql)
    usuario_db = cadasto_dao.verifica_usuario(usuario)
    if usuario_db is None:
        return False
    else:
        return True

def cria_usuario(usuario, senha):
    cadasto_dao = CadastroDao(mysql)
    cadasto_dao.cria_usuario(usuario, senha)

    