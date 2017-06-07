from AutorDAO import *
from PublicacaoDAO import *

cur = AutorDAO()

cur.consulta_autores()
cur.consulta_autor_id(1)



cur.incluir_autor(4, "Bernardo", "11111111111", 'SEVERO, B, C')
cur.consulta_autores()
cur.alterar_autor(4, "Bernardo2", "22222222222", 'SEVERO, B, C')
cur.excluir_autor(4)

cur.consulta_autores()


publicacao = PublicacaoDAO()
publicacao.consulta_Publicacao()
publicacao.incluir_publicacao(4, "inserido", 'd')
publicacao.alterar_publicacao(4, "inserido2", 'e')
publicacao.excluir_publicacao(4)

publicacao.consulta_Publicacao()

publicacao.retorna_qualis_autor(1)
publicacao.retorna_pontuacao_autor(1)


