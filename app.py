from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Atividade de Docker com Python.'

@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome,cidade):
    return jsonify({'nome':nome,'cidade':cidade})
