from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('homepage.html')

@app.route('/evento')
def evento():
   return render_template('evento.html')   

@app.route('/palestrante')
def palestrante():
   return render_template('palestrante.html')

@app.route('/semana')
def semana():
   return render_template('semana.html')

@app.route('/participante')
def participante():
   return render_template('participante.html')

@app.route('/evento/lista')
def eventoLista():
   return render_template('eventos-lista.html')

@app.route('/inscricaoEvento')
def inscricaoEvento():
    daoEvento = ControleEvento()
    daoParticipante = ControleParticipante()
    evento = daoEvento.listarTodosRegistros()
    participante = daoParticipante.listarTodosRegistros()
    
    return render_template('participante-evento.html', evento = evento, participante = participante)
   
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


@app.route('/palestrante/gravar',methods = ['POST', 'GET'])
def gravarPalestrante():
    if request.method == 'POST':
       result = request.form
       pa = Palestrante()
       pa.nome = result['nome']
       pa.email = result['email']
       pa.cpf = result['cpf']
       daoPalestrante = ControlePalestrante()

       if result['botao']=='Gravar':
           daoPalestrante.incluirPalestrante(pa)
       else:
           pa.idpalestrante=result['codigo']
           daoPalestrante.alterarEvento(pa)

    return redirect(url_for('tabelaPalestrante'))

@app.route('/evento/gravar',methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       ev = Evento()
       ev.nome = result['nome']
       ev.descricao = result['descricao']
       ev.data = result['data']
       ev.horario = result['horario']
       ev.idsemana = result['idsemana']
       ev.local = result['local']
       daoEvento = ControleEvento()

       if result['botao']=='Gravar':
           daoEvento.incluirEvento(ev)
       else:
           ev.idaluno=result['codigo']
           daoEvento.alterarEvento(ev)

    return redirect(url_for('tabela'))

@app.route('/semana/gravar',methods = ['POST', 'GET'])
def gravarSemana():
    if request.method == 'POST':
       result = request.form
       se = Semana()
       se.nome = result['nome']
       se.descricao = result['descricao']
       se.datainicio = result['datainicio']
       se.datatermino = result['datatermino']
       se.local = result['local']
       daoEvento = ControleEvento()

       if result['botao']=='Gravar':
           daoEvento.incluirEvento(se)
       else:
           se.idaluno=result['codigo']
           daoEvento.alterarEvento(se)

    return redirect(url_for('tabelaSemanas'))

@app.route('/participante/gravar',methods = ['POST', 'GET'])
def gravarParticipante():
    if request.method == 'POST':
       result = request.form
       pa = Participante()
       pa.nome = result['nome']
       pa.email = result['email']
       pa.cpf = result['cpf']
       daoParticipante = ControleParticipante()

       if result['botao']=='Gravar':
           daoParticipante.incluirParticipante(pa)

    return redirect(url_for('tabelaParticipantes'))


@app.route('/participanteEvento/gravar',methods = ['POST', 'GET'])
def gravarParticipanteEvento():
    if request.method == 'POST':
       result = request.form
       pa = EventoParticipante()
       pa.idevento = result['idevento']
       pa.idparticipante = result['idparticipante']
       daoEventoParticipante = ControleEventoParticipante()

       if result['botao']=='Gravar':
           daoEventoParticipante.incluirEventoParticipante(pa)

    return redirect(url_for('tabelaPalestrante'))

@app.route('/tabela/')
def tabela():
    daoCliente = ControleEvento()
    dados = daoCliente.listarTodosRegistros()
    return render_template("tabela-eventos.html", result=dados)

@app.route('/tabelaPalestrante')
def tabelaPalestrante():
    daoPalestrante = ControlePalestrante()
    dados = daoPalestrante.listarTodosRegistros()
    return render_template("tabela-palestrantes.html", result=dados)

@app.route('/tabelaSemanas')
def tabelaSemanas():
    daoSemana = ControleSemana()
    dados = daoSemana.listarTodosRegistros()
    return render_template("tabela-semanas.html", result=dados)

@app.route('/tabelaParticipantes')
def tabelaParticipantes():
    daoParticipante = ControleParticipante()
    dados = daoParticipante.listarTodosRegistros()
    return render_template("tabela-participantes.html", result=dados)

@app.route('/tabelaEventoParticipante')
def tabelaEventoParticipante():
    daoEvento = ControleEvento()
    daoParticipante = ControleParticipante()
    daoEventoParticipante = ControleEventoParticipante()
    eventoParticipante = daoEventoParticipante.listarTodosRegistros()
    evento = daoEvento.listarTodosRegistros()
    participante = daoParticipante.listarTodosRegistros()
    
    return render_template('tabela-eventoParticipante.html', evento = evento, participante = participante, eventoParticipante = eventoParticipante)

@app.route('/listaEventos')
def listaEvento():
    daoEvento = ControleEvento()
    dados = daoEvento.listarTodosRegistros()
    return render_template("eventos-lista.html", result=dados)

    

import sys
import subprocess as sp
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from modelo.Evento import *
from modelo.Participante import *
from modelo.Semana import *
from modelo.Participante import *
from modelo.EventoParticipante import *
from controle.ControleEventoParticipante import *
from controle.ControleEvento import *
from controle.ControlePalestrante import *
from controle.ControleSemana import *
from controle.ControleParticipante import *


if __name__ == '__main__':
   app.run(debug = True)