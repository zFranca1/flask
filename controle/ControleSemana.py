from Conectarbanco import *
from modelo.Semana import *

import datetime
from controleGenerico import *

class ControleSemana(ControleGenerico):

    def incluirSemana(self,semana):
        self.incluir(semana)

    def alterarSemana(self, semana):
        self.alterar(semana)

    def deletarSemana(self,id):
        semana = Semana()
        semana.idsemana = id
        self.delete(semana)

    def pesquisaCodigo(self,entrada):
        semana = Semana()
        semana.idpalestrante = entrada
        semana = self.procuraRegistro(semana)
        retorno = Semana()
        if len(semana) >= 1:
            retorno.idsemana = semana[0][0]
            retorno.nome = semana[0][1]
            retorno.flag = semana[0][2]
            retorno.local = semana[0][3]
            retorno.datainicio = semana[0][4]
            retorno.datatermino = semana[0][5]
            retorno.descricao = semana[0][6]

        return retorno

    def listarTodosRegistros(self):
        semana = Semana()
        return self.listarTodos(semana)



