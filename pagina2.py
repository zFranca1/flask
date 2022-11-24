from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
   a = '''Bem vindo a minha pagina <br>
          Esta pagina mostra como usar o PYTHON <br>
          Como servidor Web
          <h1> Exemplo de Titulo </h1>
          '''
   return a

@app.route('/principal')
def principal():
    return "<H3>Voce esta na pagina principal</H3>"

@app.route('/mostraaluno')
def mostraaluno():
    al = Aluno()
    daoaluno = ControleAluno()
    al.idaluno=2
    al = daoaluno.pesquisaCodigo(al)

    volta = ''' <h3>Nome completo: {} </h3>
                <h3>Endereço.....: {} </h3>
                <h3>Cidade.......: {} </h3>
                <input type='text' value='{}'>
               '''.format(al.nome,al.endereco,al.cidade,al.nome)

    return volta

@app.route('/mostra/<codigo>')
def mostra(codigo):
    al = Aluno()
    daoaluno = ControleAluno()
    al.idaluno=codigo
    al = daoaluno.pesquisaCodigo(al)

    volta = ''' <h3>Nome completo: {} </h3>
                <h3>Endereço.....: {} </h3>
                <h3>Cidade.......: {} </h3>
                <input type='text' value={}>
               '''.format(al.nome,al.endereco,al.cidade,al.nome)

    return volta

@app.route('/envio/', methods=['GET', 'POST'])
def envio():

    if request.method == 'POST':
        name = request.form['name'].upper()
    else:
        name = 'metodo get'

    return name

import sys
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from aluno import *
from controleAluno import *

if __name__ == "__main__":

   app.run(debug=True)