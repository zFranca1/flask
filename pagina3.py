from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h2>Ola Mundo, bem vindo ao site</h2>"

@app.route('/consulta/<nome>')
def consulta(nome):
    return '<h1> Bem vindo, {} </h1>'.format(nome)

@app.route('/apresenta/<nome>')
def apresenta(nome):
    volta = '''
            <h1>Ola, {}</h1>
            <p>Bem vindo</p>
            '''.format(nome)

    return volta

if __name__ == "__main__":
   app.run(debug=True)