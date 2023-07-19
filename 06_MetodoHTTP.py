""" 
GET é usado para obter dados do servidor, enquanto o método POST é usado para enviar dados ao servidor.
A escolha entre esses métodos depende do tipo de operação que você deseja realizar e do tipo de dados que você está
manipulando.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/get_example', methods=['GET'])
def get_example():
    # Lógica para lidar com uma requisição GET
    return 'Exemplo de resposta para uma requisição GET'

@app.route('/post_example', methods=['POST'])
def post_example():
    # Lógica para lidar com uma requisição POST
    data = request.form.get('nome')
    print(request.form)
    # Processar os dados enviados pelo cliente no corpo da requisição
    return f'Exemplo de resposta para uma requisição POST. Dados recebidos: {data}'

app.run()
