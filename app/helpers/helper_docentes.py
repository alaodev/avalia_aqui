from app import mysql
from app.models.docentes_dao import DocentesDao

def lista_docentes():
    docentes_dao = DocentesDao(mysql)
    docentes_db = docentes_dao.lista_docentes()
    docentes_media = []

    for dado in docentes_db: # Cria uma lista contento o nome do professor e sua média geral.
        if dado[2] is None:
            docentes_media.append([dado[0], dado[1], 'Não Avaliado'])
        else:
            media = sum([dado[2], dado[3], dado[4], dado[5], dado[6]])/5
            docentes_media.append([dado[0], dado[1], "%.1f" % round(media,2), dado[7]])

    return docentes_media

def busca_professor(id_professor):
    docentes_dao = DocentesDao(mysql)
    professor_db = docentes_dao.busca_professor(id_professor)

    return professor_db

def media_avaliacoes(id_professor):
    docentes_dao = DocentesDao(mysql)
    try:
        media_avaliacoes = ["%.2f" % round(media,2) for media in docentes_dao.media_avaliacoes(id_professor)]
    except:
        media_avaliacoes = ['Não avaliado' for media in range(5)]


    return media_avaliacoes

def ultima_avaliacao(id_usuario, id_professor):
    docentes_dao = DocentesDao(mysql)
    ultima_avaliacao = docentes_dao.ultima_avaliacao(id_usuario, id_professor)

    if ultima_avaliacao is None:
        ultima_avaliacao = ['Não avaliado' for media in range(5)]

    return ultima_avaliacao

def top3():
    docentes_dao = DocentesDao(mysql)
    docentes_db = docentes_dao.lista_docentes()
    top = []
    for docente in docentes_db:
        if docente[2] is None:
            top.append([docente[1], 0, docente[7], 0])
        else:
            media =  float("%.2f" % round(sum([docente[2], docente[3], docente[4], docente[5], docente[6]])/5,2))
            top.append([docente[1], media, docente[7], float("%.2f" % round(media*docente[7], 2))])
    top = sorted(top, key = lambda x: (x[3], x[2]), reverse = True)

    return top[0:3]