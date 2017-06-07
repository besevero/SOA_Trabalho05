import Infra



class PublicacaoDAO(object):

    def __init__(self):
        pass

    def consulta_Publicacao(self):

        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""SELECT * from artigo""")
        except:
            print "Empty data table Autor"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row

        return rows

    def consulta_publicacao_id(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""SELECT * FROM artigo WHERE id_artigo = (%s)""", (id,))
        except:
            print "Empty data table Autor por id"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row
        return rows

    def incluir_publicacao(self, id_artigo, nome, tipoartigo):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""INSERT INTO artigo VALUES(%s,%s,%s);""", (id_artigo, nome, tipoartigo))
            conn.commit()
            print "Inserido com sucesso!"
        except:
            print "Erro incluir"

    def alterar_publicacao(self, id, nome, tipoartigo):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""UPDATE artigo SET nome = (%s), tipoartigo = (%s) WHERE id_artigo = (%s);""", (nome, tipoartigo, id))
            conn.commit()
            print "Alterado com sucesso!"
        except:
            print "Erro alterar por id"

    def excluir_publicacao(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""DELETE FROM artigo WHERE id_artigo = (%s);""", (id,))
            conn.commit()
            print "Excluido com sucesso!"
        except:
            print "Erro delete"

    def consulta_geral(self):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""select a.citacao , b.nome ,  f.nome || ' ' || '('||f.sigla||')', e.ano from Artigo b, ArtigoEdicao c, AutorArtigo d, Autor a, Edicao e, Forum f where b.id_artigo = c.id_artigo and b.id_artigo = d.id_artigo and 
a.id_autor = d.id_autor and c.id_edicao = e.id_edicao and e.id_forum = f.id_forum;""")

        except:
            print "Empty data table Autor"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row

        return rows

    def retorna_qualis_autor(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""select b.nome, q.codqualis from Artigo b, ArtigoEdicao c, AutorArtigo d, Autor a, Edicao
        e, Qualis q, Forum f where b.id_artigo = c.id_artigo and b.id_artigo = d.id_artigo and
        a.id_autor = d.id_autor and c.id_edicao = e.id_edicao and e.id_forum = f.id_forum and e.id_qualis = q.id_qualis 
        and a.id_autor = (%s);""", (id, ))

        except:
            print "Autor nao possui qualis"

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:
            print "   ", row

        return rows

    def retorna_pontuacao_autor(self, id):
        conn = Infra.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""select a.nome, q.peso from Artigo b, ArtigoEdicao c, AutorArtigo d, Autor a, Edicao
        e, Qualis q, Forum f where b.id_artigo = c.id_artigo and b.id_artigo = d.id_artigo and
        a.id_autor = d.id_autor and c.id_edicao = e.id_edicao and e.id_forum = f.id_forum and e.id_qualis = q.id_qualis 
        and a.id_autor = (%s);""", (id, ))

        except:
            print "Autor nao possui qualis"

        rows = cur.fetchall()
        print "\nRows: \n"
        count = 0
        for row in rows:
            count = count + row[1]
            print "   ", row
        print row[0], 'possui pontuacao de:', count
        return row[0], count