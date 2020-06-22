from app import mysql
from app.models.login_dao import LoginDao

def valida_login(usuario, senha): # True = Login válido. False = Login inválido.
    login_dao = LoginDao(mysql)
    usuario_db = login_dao.valida_login(usuario)
    if usuario_db is not None and usuario_db[2] == senha:
        return usuario_db
    else:
        return False

def busca_usuario_id(id_usuario):
    login_dao = LoginDao(mysql)
    usuario_db = login_dao.busca_usuario_id(id_usuario)
    
    return usuario_db