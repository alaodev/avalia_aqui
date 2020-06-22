SQL_CRIA_AVALIACAO = 'INSERT INTO avaliacao (nota1, nota2, nota3, nota4, nota5, fk_usuario, fk_professor) VALUES (%s, %s, %s, %s, %s, %s, %s)'
SQL_VERIFICA_AVALIACAO = 'SELECT * FROM avaliacao WHERE fk_usuario = %s'
SQL_VERIFICA_AVALIACAO_PROFESSOR = 'SELECT * FROM avaliacao WHERE fk_usuario = %s AND fk_professor = %s'
SQL_ALTERA_AVALIACAO = 'UPDATE avaliacao SET nota1 = %s, nota2 = %s, nota3 = %s, nota4 = %s, nota5 = %s WHERE fk_usuario = %s AND fk_professor = %s'
SQL_CONTA_NUM_AVALIACOES = 'SELECT COUNT(*) FROM avaliacao WHERE fk_professor = %s'

class AvaliacaoDao:
    def __init__(self, db):
        self.db = db

    def cria_avaliacao(self, nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_CRIA_AVALIACAO, (nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor, ))
        self.db.connection.commit()

    def verifica_avaliacao(self, id_usuario):
        cur = self.db.connection.cursor()
        cur.execute(SQL_VERIFICA_AVALIACAO, (id_usuario))
        avaliacao_db = cur.fetchall()

        return avaliacao_db

    def verifica_avaliacao_professor(self, id_usuario, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_VERIFICA_AVALIACAO_PROFESSOR, (id_usuario, id_professor, ))
        avaliacao_db = cur.fetchall()

        return avaliacao_db

    def altera_avaliacao(self, nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_ALTERA_AVALIACAO, (nota1, nota2, nota3, nota4, nota5, id_usuario, id_professor, ))
        self.db.connection.commit()

    def conta_num_avaliacoes(self, id_professor):
        cur = self.db.connection.cursor()
        cur.execute(SQL_CONTA_NUM_AVALIACOES, (id_professor))
        avaliacao_db = cur.fetchone()