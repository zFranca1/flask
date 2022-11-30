from Conectarbanco import *
from modelo.Participante import *

import datetime
from controleGenerico import *

class ControleParticipante(ControleGenerico):

    def incluirParticipante(self,participante):
        self.incluir(participante)

    def alterarParticipante(self, participante):
        self.alterar(participante)

    def deletarParticipante(self,id):
        participante = Participante()
        participante.idparticipante = id
        self.delete(participante)

    def pesquisaCodigo(self,entrada):
        participante = Participante()
        participante.idparticipante = entrada
        participante = self.procuraRegistro(participante)
        retorno = Participante()
        if len(participante) >= 1:
            retorno.idpalestrante = participante[0][0]
            retorno.nome = participante[0][1]
            retorno.flag = participante[0][2]
            retorno.email = participante[0][3]
            retorno.cpf = participante[0][4]

        return retorno

    def listarTodosRegistros(self):
        participante = Participante()
        return self.listarTodos(participante)



