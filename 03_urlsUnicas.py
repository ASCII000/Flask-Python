from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Olá Mundo!"

@app.route('/sobre/') # Neste caso há barras de ambos lados significando que o redirecionando idepende de haver barras ou nao
def sobre():          # Será dada ao /sobre
    return "Olá está é a Guia sobre!"

app.run()
