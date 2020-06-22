SQL_LISTA_PROFESSORES = 'SELECT * FROM professor'
SQL_LISTA_DOCENTES = 'SELECT professor.id_professor, professor.nome, AVG(avaliacao.nota1), AVG(avaliacao.nota2), AVG(avaliacao.nota3), AVG(avaliacao.nota4), AVG(avaliacao.nota5),COUNT(*) FROM professor LEFT JOIN avaliacao ON professor.id_professor = avaliacao.fk_professor GROUP BY professor.nome'
SQL_BUSCA_PROFESSOR = 'SELECT * FROM professor WHERE id_professor = %s'
SQL_MEDIA_AVALIACOES = 'SELECT AVG(nota1), AVG(nota2), AVG(nota3), AVG(nota4), AVG(nota5) FROM avaliacao WHERE fk_professor = %s'
SQL_ULTIMA_AVALIACAO = 'SELECT nota1, nota2, nota3, nota4, nota5 FROM avaliacao WHERE fk_usuario = %s AND fk_professor = %s;'

class DocentesDao:
    def __init__(self, db):
        self.db = db

    def lista_professores(self):
        cur = self.db.connection.cursor()
        cur.execute(SQL_LISTA_PROFESSORES)
        professores_db = cur.fetchall()

        return medias_db

    def lista_docentes(self):
        cur = self.db.connection.cursor()
        cur.execute(SQL_LISTA_DOCENTES)
        medias_db = cur.fetchall()

        return medias_db

    def busca_professor(self, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_BUSCA_PROFESSOR, (id_professor, ))
        professor_db = cur.fetchone()

        return professor_db

    def media_avaliacoes(self, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_MEDIA_AVALIACOES, (id_professor, ))
        media_avaliacoes_db = cur.fetchone()

        return media_avaliacoes_db

    def ultima_avaliacao(self, id_usuario, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_ULTIMA_AVALIACAO, (id_usuario, id_professor, ))
        ultima_avaliacao_db = cur.fetchone()

        print(ultima_avaliacao_db)

        return ultima_avaliacao_db