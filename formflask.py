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
    daoCliente = ControleCliente()
    dados = daoCliente.pesquisaCodigo(id)
    return render_template("editaestudante.html",dados = dados)

@app.route('/delete/<id>')
def delete(id):
    daoCliente = ControleCliente()
    daoCliente.deleteCliente(id)
    return redirect(url_for('tabela'))

@app.route('/gravar',methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       cl = Cliente()
       cl.nome = result['nome']
       cl.endereco = result['endereco']
       cl.cidade = result['cidade']
       cl.uf = result['uf']
       cl.cep = result['cep']
       cl.nascimento = result['data']
       daoCliente = ControleCliente()

       if result['botao']=='Gravar':
           daoCliente.incluirCliente(cl)
       else:
           cl.idaluno=result['codigo']
           daoCliente.alterarCliente(cl)

    return redirect(url_for('tabela'))

@app.route('/tabela/')
def tabela():
    daoCliente = ControleCliente()
    dados = daoCliente.listarTodosRegistros()
    return render_template("resultadotabela.html", result=dados)

import sys
import subprocess as sp
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from modelo.Cliente import *
from controle.ControleCliente import *

if __name__ == '__main__':
   app.run(debug = True)