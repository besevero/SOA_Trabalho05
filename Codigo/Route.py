from flask import Flask, jsonify
from AutorDAO import *
from PublicacaoDAO import *

app = Flask(__name__)

artigo = PublicacaoDAO()

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/trab05/autores', methods=['GET'])
def get_autores():
    autor = AutorDAO()
    autores = autor.consulta_autores()
    return jsonify(autores)


@app.route('/trab05/autores/<int:id>', methods=['GET'])
def get_autores_id(id):
    autor = AutorDAO()
    autores_id = autor.consulta_autor_id(id)
    return jsonify(autores_id)


@app.route('/trab05/autores/<int:id>/<string:nome>/<string:cpf>', methods=['POST'])
def post_autores_id(id, nome, cpf):
    autor = AutorDAO()
    autor.incluir_autor(id, nome, cpf)
    return jsonify({'result': True})


@app.route('/trab05/autores/<int:id>/<string:nome>/<string:cpf>', methods=['PUT'])
def update_autores_id(id, nome, cpf):
    autor = AutorDAO()
    autor.alterar_autor(id, nome, cpf)
    return jsonify({'result': True})


@app.route('/trab05/autores/<int:id>', methods=['DELETE'])
def delete_autor(id):
    autor = AutorDAO()
    autor.excluir_autor(id)
    return jsonify({'result': True})

@app.route('/trab05/artigo', methods=['GET'])
def get_artigos():
    artigos = artigo.consulta_Publicacao()
    return jsonify(artigos)


@app.route('/trab05/artigos/<int:id>', methods=['GET'])
def get_artigos_id(id):
    artigo_id = artigo.consulta_Publicacao(id)
    return jsonify(artigo_id)


@app.route('/trab05/artigo/<int:id>/<string:nome>/<string:tipo>', methods=['POST'])
def post_artigo_id(id, nome, tipo):
    artigo.incluir_publicacao(id, nome, tipo)
    return jsonify({'result': True})


@app.route('/trab05/artigos/<int:id>/<string:nome>/<string:tipo>', methods=['PUT'])
def update_artigo_id(id, nome, tipo):
    artigo.alterar_publicacao(id, nome, tipo)
    return jsonify({'result': True})


@app.route('/trab05/artigos/<int:id>', methods=['DELETE'])
def delete_artigo(id):
    artigo.excluir_publicacao(id)
    return jsonify({'result': True})

@app.route('/trab05/artigos/', methods=['GET'])
def get_artigos_citacao():
    artigos = artigo.consulta_geral()
    return jsonify(artigos)


@app.route('/trab05/qualis/<int:id>', methods=['GET'])
def get_qualis(id):
    qualis = artigo.retorna_qualis_autor(id)
    return jsonify(qualis)


@app.route('/trab05/pontuacao/autor/<int:id>', methods=['GET'])
def get_soma_qualis(id):
    qualis = artigo.retorna_pontuacao_autor(id)
    return jsonify(qualis)


@app.route('/trab05/pontuacaoartigo/autor/<int:id>', methods=['GET'])
def get_pontuacao_artigo_qualis(id):
    qualis = artigo.retorna_pontuacao_autor(id)
    autor = AutorDAO()
    autores_id = autor.consulta_autor_id(id)
    return jsonify(autores_id, qualis)


if __name__ == '__main__':
        app.run(debug=True)

