from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    daoSemana = ControleSemana()
    dados = daoSemana.listarTodosRegistros()

    return render_template('homepage.html', result = dados)

@app.route('/evento')
def evento():

    daoPalestrante = ControlePalestrante()
    daoSemana = ControleSemana()
    palestrante = daoPalestrante.listarTodosRegistros()
    semana = daoSemana.listarTodosRegistros()

    return render_template('evento.html', evento = evento, palestrante = palestrante, semana = semana)  

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
   

@app.route('/editar/<id>')
def editar(id):
    daoCliente = ControleEvento()
    dados = daoCliente.pesquisaCodigo(id)
    return render_template("editaestudante.html",dados = dados)

@app.route('/deleteParticipante/<id>')
def deleteParticipante(id):
    daoParticipante = ControleParticipante()
    daoParticipante.deletarParticipante(id)
    return redirect(url_for('tabelaParticipantes'))

@app.route('/deletePalestrante/<id>')
def deletePalestrante(id):
    daoPalestrante = ControlePalestrante()
    daoPalestrante.deletarPalestrante(id)
    return redirect(url_for('tabelaPalestrante'))

@app.route('/deleteEvento/<id>')
def deleteEvento(id):
    daoEvento = ControleEvento()
    daoEvento.deletarEvento(id)
    return redirect(url_for('tabela'))

@app.route('/deleteSemana/<id>')
def deleteSemana(id):
    daoSemana = ControleSemana()
    daoSemana.deletarSemana(id)
    return redirect(url_for('tabelaSemanas'))      

@app.route('/deleteEventoParticipante/<idevento>,<idparticipante>')
def deleteEventoParticipante(idevento,idparticipante):
    daoEventoParticipante = ControleEventoParticipante()
    daoEventoParticipante.deletarEventoParticipante(idevento,idparticipante)
    return redirect(url_for('tabelaEventoParticipante'))

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
       ev.idpalestrante = result['idpalestrante']
       ev.idsemana = result['idsemana']
       daoEvento = ControleEvento()
       

       if result['botao']=='Gravar':
           daoEvento.incluirEvento(ev)

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

    return redirect(url_for('tabelaEventoParticipante'))


@app.route('/palestranteEvento/gravar',methods = ['POST', 'GET'])
def gravarPalestranteEvento():
    if request.method == 'POST':
       result = request.form
       pa = EventoPalestrante()
       pa.idevento = result['idevento']
       pa.idpalestrante = result['idparticipante']
       pa.idsemana = result['idsemana']
       daoEventoPalestrante = ControleEventoPalestrante()

       if result['botao']=='Gravar':
           daoEventoPalestrante.incluirEventoParticipante(pa)
           

    return redirect(url_for('tabelaPalestrante'))    

@app.route('/tabela/')
def tabela():
    daoCliente = ControleEvento()
    daoPalestrante = ControlePalestrante()
    palestrante = daoPalestrante.listarTodosRegistros()
    dados = daoCliente.listarTodosRegistros()
    return render_template("tabela-eventos.html", result=dados, palestrante = palestrante)

@app.route('/eventos')
def eventos():
    daoCliente = ControleEvento()
    daoPalestrante = ControlePalestrante()
    palestrante = daoPalestrante.listarTodosRegistros()
    dados = daoCliente.listarTodosRegistros()
    return render_template("eventos-lista.html", result=dados, palestrante = palestrante)    

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


import sys
import subprocess as sp
sys.path.insert(0, 'modelo')
sys.path.insert(1, 'controle')
from modelo.Evento import *
from modelo.Participante import *
from modelo.Semana import *
from modelo.Participante import *
from modelo.EventoParticipante import *
from modelo.EventoParticipante import *
from controle.ControleEventoParticipante import *
from controle.ControleEvento import *
from controle.ControlePalestrante import *
from controle.ControleSemana import *
from controle.ControleParticipante import *
from controle.ControleEventoPalestrante import *


if __name__ == '__main__':
   app.run(debug = True)