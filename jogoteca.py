# APP Utilizando o framework Flask
# flask: referencio à Biblioteca flask e Flask: importando a função Flask para a construção da aplicação
# o flask não é uma função embutida do python, vou ter que importar no terminal com PiP

from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return '<h1>Olá Mundo!</h1>'

app.run()
