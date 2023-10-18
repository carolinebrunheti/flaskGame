from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route('/', methods=("GET", "POST"))
def index():
    if request.method =="GET":
        variavel = "Game: Adivinhe o numero correto"
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1,20)
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return '<h1>Resultado: Voce Ganhou</h1>'
        else:
            return '<h1>Resultado: Voce Perdeu</h1>'
    
    

@app.route('/sobre')
def sobre():
    return 'Sobre'

@app.route('/<string:nome>')
def error(nome):
    variavel = f'Pagina ({nome}) nao existe'
    return render_template("error.html", variavel=variavel)