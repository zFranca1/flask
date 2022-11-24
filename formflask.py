from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('estudante.html')

@app.route('/teste')
def teste():
   #Usando arquivo PHP
   out = sp.run(["php", "templates/estudantephp.php"], stdout=sp.PIPE)
   return out.stdout

@app.route('/editar/<id>')
def editar(id):
    daoCliente = ControleEvento()
    dados = daoCliente.pesquisaCodigo(id)
    return render_template("editaestudante.html",dados = dados)

@app.route('/delete/<id>')
def delete(id):
    daoEvento = ControleEvento()
    daoEvento.deleteEvento(id)
    return redirect(url_for('tabela'))

@app.route('/gravar',methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       ev = Evento()
       ev.nome = result['nome']
       ev.descricao = result['descricao']
       daoEvento = ControleEvento()

       if result['botao']=='Gravar':
           daoEvento.incluirEvento(ev)
       else:
           ev.idaluno=result['codigo']
           daoEvento.alterarEvento(ev)

    return redirect(url_for('tabela'))

@app.route('/tabela/')
def tabela():
    daoCliente = ControleEvento()
    dados = daoCliente.listarTodosRegistros()
    return render_template("resultadotabela.html", result=dados)

import sys
import subprocess as sp
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from modelo.Evento import *
from controle.ControleEvento import *

if __name__ == '__main__':
   app.run(debug = True)