from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

artigos = {
    'Receita de bolo':{
        'subtitulo':'Quer uma receita de bolo simples e gostoso?',
        'conteudo':'Quer um bolo simples, bem gostoso e fofinho para o café da tarde? Encontrou! Confira como fazer essa receita de bolo simples, também conhecido como bolo de farinha de trigo. Ele cai muito bem com um café quentinho!'},
    
    'Receita de pão de queijo':{
        'subtitulo':'Uma recomendação de um bom pão de queijo',
        'conteudo':'Quem não gosta de pão de queijo, certamente tem desvio de caráter! Descubra como fazer aquela massa fofinha e arrase no preparo do seu pão de queijo caseiro!'},
    'Receita de pudim legal':{
        'subtitulo':'Uma simples receita de pudim',
        'conteudo':'Receita'
    }
}

@app.route('/')
def index():
    return render_template('login.jinja2')

@app.route('/view', methods=['POST'])
def view():
    nome =  request.form['nomeForm']
    idade = request.form['idade']

    return render_template('index.jinja2', nome=nome, idade=idade, artigos=artigos)

@app.route('/artigo/<titulo>')
def artigo(titulo):
    artigo = artigos.get(titulo)
    print(artigo)
    if artigo:
        return render_template('artigo.jinja2', titulo=titulo, subtitulo=artigo['subtitulo'], conteudo=artigo['conteudo'])
    else:
        return 'Artigo não encontrado'

# Rota para importar os arquivos estaticos do programa
@app.route('/07_RenderTemplates/static/<path:filename>')
def ffStatic(filename):
    return send_from_directory('static', filename)

if __name__=='__main__':
    app.run(debug=True)
