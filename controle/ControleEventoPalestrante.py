from Conectarbanco import *
from modelo.EventoPalestrante import *

import datetime
from controleGenerico import *

class ControleEventoPalestrante(ControleGenerico):

    def incluirEventoPalestrante(self,eventoParticipante):
        self.incluir(eventoParticipante)


    def listarTodosRegistros(self):
        eventoPalestrante = EventoPalestrante()
        return self.listarTodos(eventoPalestrante)



