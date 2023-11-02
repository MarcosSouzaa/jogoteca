# APP Utilizando o framework Flask
# flask: referencio à Biblioteca flask e Flask: importando a função Flask para a construção da aplicação
# o flask não é uma função embutida do python, vou ter que importar no terminal com PiP

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run()
