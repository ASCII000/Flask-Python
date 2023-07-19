from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#  Roteamento
@app.route('/')
def helloWorld():
    return "Olá Mundo!"

# Receber uma variavel como nome de um sessão -> <nome_da_variavel>
@app.route('/ola/<name>')
def hello(name):
    return f"Olá, {escape(name)}!"

app.run()
