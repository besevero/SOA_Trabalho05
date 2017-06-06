from flask import Flask
from AutorDAO import *


app = Flask(__name__)

cur = AutorDAO()

cur.consulta_autores()
cur.consulta_autor_id(1)



cur.incluir_autor(4, "Bernardo", "11111111111")
cur.alterar_autor(4, "Bernardo2", "22222222222")
cur.excluir_autor(4)

cur.consulta_autores()
