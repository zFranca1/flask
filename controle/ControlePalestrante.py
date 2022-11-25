from Conectarbanco import *
from modelo.Palestrante import *

import datetime
from controleGenerico import *

class ControlePalestrante(ControleGenerico):

    def incluirPalestrante(self, palestrante):
        self.incluir(palestrante)

    def alterarPalestrante(self, palestrante):
        self.alterar(palestrante)

    def deletarPalestrante(self,id):
        palestrante = Palestrante()
        palestrante.idpalestrante = id
        self.delete(palestrante)

    def pesquisaCodigo(self,entrada):
        palestrante = Palestrante()
        palestrante.idpalestrante = entrada
        palestrante = self.procuraRegistro(palestrante)
        retorno = Palestrante()
        if len(palestrante) >= 1:
            retorno.idpalestrante = palestrante[0][0]
            retorno.nome = palestrante[0][1]
            retorno.flag = palestrante[0][2]
            retorno.email = palestrante[0][3]
            retorno.cpf = palestrante[0][4]

        return retorno

    def listarTodosRegistros(self):
        palestrante = Palestrante()
        return self.listarTodos(palestrante)

    def converteObjeto(self,entrada):
        palestrante = Palestrante()
        palestrante.idevento=entrada[0]
        palestrante.nome=entrada[1]
        palestrante.endereco=entrada[2]

        return palestrante

    def dadosJson(self,entrada):
        pesquisa = self.procuraRegistro(entrada)
        dados = Palestrante()
        dados = self.converteObjeto(pesquisa[0])
        retorno = {}
        retorno = {'idevento': dados.idevento,
                   'nome': dados.nome,
                   'flag': dados.flag,
                   'descricao': dados.descricao,}
        return json.dumps(retorno)


