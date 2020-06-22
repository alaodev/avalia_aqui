from app import mysql
from app.models.avaliacao_dao import AvaliacaoDao

def cria_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor):
    avaliacao_dao = AvaliacaoDao(mysql)
    avaliacao_dao.cria_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor)

def verifica_avaliacao(id_usuario):
    avaliacao_dao = AvaliacaoDao(mysql)
    avaliacao_db = avaliacao_dao.verifica_avaliacao(id_usuario)

    return avaliacao_db

def verifica_avaliacao_professor(id_usuario, id_professor): # True = Já avaliou o professor. False = Não avaliou.
    avaliacao_dao = AvaliacaoDao(mysql)
    avaliacao_db = avaliacao_dao.verifica_avaliacao_professor(id_usuario, id_professor)
    if avaliacao_db:
        return True
    else:
        return False

def altera_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor):
    avaliacao_dao = AvaliacaoDao(mysql)
    avaliacao_dao.altera_avaliacao(nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor)

def conta_num_avaliacoes(id_professor):
    avaliacao_dao = AvaliacaoDao(mysql)
    avaliacao_db = avaliacao_dao.conta_num_avaliacoes(id_professor)

    return avaliacao_db