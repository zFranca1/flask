from datetime import date, datetime

class EventoParticipante:

    def __init__(self):

        self.__idevento=""
        self.__idparticipante=""
        self.__lista='idevento,idparticipante'

        self.__dadosInserir=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'eventoxparticipante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}'".format(self.idevento, self.idparticipante)
        return self.__dadosInserir


    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idevento={} and idparticipante={}".format(self.idevento,self.idparticipante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idaluno={}".format(self.idparticipante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idparticipante(self):
        return self.__idparticipante

    @idparticipante.setter
    def idparticipante(self, entrada):
        self.__idparticipante = entrada

    @property
    def idevento(self):
        return self.__idevento

    @idevento.setter
    def idevento(self,entrada):
        self.__idevento=entrada


    def __repr__(self):
        return  self.idevento

