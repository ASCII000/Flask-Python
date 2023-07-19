"""
Você pode adicionar seções variáveis a um URL marcando as seções com <variable_name>.
Sua função então recebe o <variable_name> como um argumento de palavra-chave. Opcionalmente,
você pode usar um conversor para especificar o tipo de argumento como <converter:variable_name>.

/----Tipos de conversores:
string ->(padrão) aceita qualquer texto sem barra
int    -> aceita inteiros positivos
float  -> aceita valores positivos de ponto flutuante
path   -> gosto string, mas também aceita barras
uuid   -> aceita strings UUID
"""

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

posts = {
    1: 'Olá este é o 1º primeiro post!',
    2: 'Olá este é o segundo post!',
    3: 'Olá este é o terceiro post!'
}
_artigos = {
    'Como fazer receita de bolo':'Quer um bolo simples, bem gostoso e fofinho para o café da tarde? Encontrou! Confira como fazer essa receita de bolo simples, também conhecido como bolo de farinha de trigo. Ele cai muito bem com um café quentinho!',
    'Cuide da sua saúde':'A saúde é considerada o equilíbrio existente dentro de uma pessoa, é a sua qualidade de vida, estar próximo das pessoas que você ama, é conseguir realizar os seus sonhos. Além disso, é o estado',
    'Exercicios basicos para saúde':'Atividade física é qualquer movimento voluntário produzido pela musculatura que resulte num gasto de energia acima do nível de repouso. Exemplos, passear com o cachorro, dançar, entre outros.'
}

@app.route('/')
def PaginaInicial():
    listaPosts = '<h1>Seja bem vindo ao nosso Blog!</h1>'
    for conteudoArtigo in _artigos:
        listaPosts += f'<a href={url_for("artigos", artigo=conteudoArtigo)}>Leia mais sobre o artigo: {conteudoArtigo}</a><br>'

    for post_id in posts:
        listaPosts += f'<a href="{url_for("usuario", post=post_id)}">Veja o {post_id:04}º do website<a><br>'

    return listaPosts

@app.route('/post/<int:post>')
def usuario(post):
    return f'Post: {posts.get(post, "Post não encontrado.")}'

@app.route('/artigo/<string:artigo>')
def artigos(artigo):
    
    return f'<h1>{artigo}</h1><br><br><p>{_artigos.get(artigo, "Artigo não existente")}</p>'

app.run()