from os import abort

from flask import Flask, jsonify
from flask import request

from AutorDAO import *

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

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


@app.route('/trab05/autores/teste/<int:id>', methods=['DELETE'])
def delete_autor(id):
    autor = AutorDAO()
    autor.excluir_autor(id)
    return jsonify({'result': True})


@app.route('/trab05/autor/post/<int:id>', methods=['POST'])
def post_autores_id(id):
    autor = AutorDAO()
    autor.incluir_autor(id, 'Bernardo', "22222222222")
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

