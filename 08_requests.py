from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None

    if request.method == 'POST':
        return 'Método POST'
    
    else:
        return 'Invalid Request'

app.run()
