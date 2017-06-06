import psycopg2

import Infra



class AutorDAO(object):
    def __init__(self):
        pass

    def consulta_autores(self):

        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""SELECT * from Autor""")
        except:
            print "Empty data table Autor"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row

        return rows

    def consulta_autor_id(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""SELECT * FROM Autor WHERE id_autor = (%s)""", (id,))
        except:
            print "Empty data table Autor por id"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row
        return rows

    def incluir_autor(self, id, nome, cpf):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""INSERT INTO Autor VALUES(%s,%s,%s);""", (id, nome, cpf))
            conn.commit()
            print "Inserido com sucesso!"
        except:
            print "Erro incluir"

    def alterar_autor(self, id, nome, cpf):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""UPDATE Autor SET nome = (%s), cpf = (%s) WHERE id_autor = (%s);""", (nome, cpf, id))
            conn.commit()
            print "Alterado com sucesso!"
        except:
            print "Erro alterar por id"

    def excluir_autor(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""DELETE FROM Autor WHERE id_autor = (%s);""", (id,))
            conn.commit()
            print "Excluido com sucesso!"
        except:
            print "Erro delete"
    #Fabricio Felipe





#