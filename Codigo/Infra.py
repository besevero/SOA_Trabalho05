import psycopg2


def conectar():
    # Try to connect
    try:
        conn = psycopg2.connect("dbname='trab_05' user='postgres' password='admin'")
    except:
        print "Nao foi possivel acessar o banco de dados."
    return conn