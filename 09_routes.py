from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Página inicial"

@app.route('/admin')
def admin():
    return "Página de administração"

@app.route('/api', host='api.example.com')
def api():
    return "API da aplicação"

if __name__ == '__main__':
    app.run(debug=True)