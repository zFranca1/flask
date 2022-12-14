from Conectarbanco import *
from modelo.Evento import *

import datetime
from controleGenerico import *

class ControleEvento(ControleGenerico):

    def incluirEvento(self,evento):
        self.incluir(evento)

    def alterarEvento(self, evento):
        self.alterar(evento)

    def deletarEvento(self,id):
        evento = Evento()
        evento.idevento = id
        self.delete(evento)

    def pesquisaCodigo(self,entrada):
        evento = Evento()
        evento.idevento = entrada
        evento = self.procuraRegistro(evento)
        retorno = Evento()
        if len(evento) >= 1:
            retorno.idevento = evento[0][0]
            retorno.nome = evento[0][1]
            retorno.flag = evento[0][2]
            retorno.descricao = evento[0][3]
            retorno.data = evento[0][4]
            retorno.horaio = evento[0][5]
            retorno.idsemana = evento[0][6]
            retorno.local = evento[0][7]
            retorno.idpalestrante = evento[0][8]

        return retorno

    def listarTodosRegistros(self):
        evento = Evento()
        return self.listarTodos(evento)

    def converteObjeto(self,entrada):
        evento = Evento()
        evento.idevento=entrada[0]
        evento.nome=entrada[1]
        evento.endereco=entrada[2]

        return evento

    def dadosJson(self,entrada):
        pesquisa = self.procuraRegistro(entrada)
        dados = Evento()
        dados = self.converteObjeto(pesquisa[0])
        retorno = {}
        retorno = {'idevento': dados.idevento,
                   'nome': dados.nome,
                   'flag': dados.flag,
                   'descricao': dados.descricao,}
        return json.dumps(retorno)


