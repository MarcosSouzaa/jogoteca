# APP Utilizando o framework Flask
# flask: referencio à Biblioteca flask e Flask: importando a função Flask para a construção da aplicação
# o flask não é uma função embutida do python, vou ter que importar no terminal com PiP
# Vou criar a variável app para iniciar o projeto
# vou criara a rota para chamar no browser
# Vou criar a função ola() que vai retornar o arquivo html criado quando chamada com app.run()
# vou deixar o html dinâmico
# request ajuda pegar as informações do formulário

from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


# criando a lista de jogos para interagir com html ex: vou estanciar  a class jogo
# criando o objeto com nome, categoria e console
# Deixando a Lista global
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of war', 'Rack on Slash', 'PS2')
jogo3 = Jogo('Mortal Combate', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    # Aqui eu pego as informações enviadas pelo formulário
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    # Agora vou criar um Objeto com essas categorias e depois vou adcioná-las a uma lista
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


app.run(debug=True)
