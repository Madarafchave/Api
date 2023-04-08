from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

personagens = [
    {
        'id': 1,
        'nome': 'teste',
        'descrição': 'descrição teste',
        'link_imagem': 'link.com',
        'programa': 'Disney',
        'animador': 'testador',
    },
    {
        'id': 2,
        'nome': 'teste2',
        'descrição': 'descrição teste2',
        'link_imagem': 'link.com2',
        'programa': 'Disney2',
        'animador': 'testador2',
    }
]

# consultar os personagens


@app.route('/personagens', methods=['POST'])
def criar_personagem():
    novo_personagem = request.get_json()
    personagens.append(novo_personagem)
    return jsonify(personagens)


@app.route('/personagens', methods=['GET'])
def visualizar_personagem():
    return jsonify(personagens)


@app.route('/personagens/<int:id>', methods=['GET'])
def vizualizar_personagens_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem)


@app.route('/personagens/<int:id>', methods=['PUT'])
def editar_personagem_por_id(id):
    personagem_editado = request.get_json()
    for indice, personagem in enumerate(personagens):
        if personagens.get('id') == id:
            personagens[indice].update(personagem_editado)
            return jsonify(personagens[indice])


app.run(port=5000, host='localhost', debug=True)
