# APP Utilizando o framework Flask
# flask: referencio à Biblioteca flask e Flask: importando a função Flask para a construção da aplicação
# o flask não é uma função embutida do python, vou ter que importar no terminal com PiP
# Vou criar a variável app para iniciar o projeto
# vou criara a rota para chamar no browser
# Vou criar a função ola() que vai retornar o arquivo html criado quando chamada com app.run()
# vou deixar o html dinâmico

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    # criando a lista de jogos para interagir com html
    lista = ['Tetris', 'Skirim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
