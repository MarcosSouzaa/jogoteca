# APP Utilizando o framework Flask
# flask: referencio à Biblioteca flask e Flask: importando a função Flask para a construção da aplicação
# o flask não é uma função embutida do python, vou ter que importar no terminal com PiP
# Vou criar a variável app para iniciar o projeto
# vou criara a rota para chamar no browser
# Vou criar a função ola() que vai retornar o arquivo html criado quando chamada com app.run()
# vou deixar o html dinâmico

from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    # criando a lista de jogos para interagir com html ex: vou estanciar  a class jogo
    # criando o objeto com nome, categoria e console

    jogo1 = jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = jogo('God of war', 'Rack on Slash', 'PS2')
    jogo3 = jogo('Mortal Combate', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

app.run()
