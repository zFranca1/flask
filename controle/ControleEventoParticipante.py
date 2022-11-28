from Conectarbanco import *
from modelo.EventoParticipante import *

import datetime
from controleGenerico import *

class ControleEventoParticipante(ControleGenerico):

    def incluirEventoParticipante(self,eventoParticipante):
        self.incluir(eventoParticipante)


    def listarTodosRegistros(self):
        eventoParticipante = EventoParticipante()
        return self.listarTodos(eventoParticipante)



