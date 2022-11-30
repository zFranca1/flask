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

    def deletarEventoParticipante(self,idevento, idparticipante):
        eventoParticipante = EventoParticipante()
        eventoParticipante.idevento = idevento
        eventoParticipante.idparticipante = idparticipante
        self.delete(eventoParticipante)
