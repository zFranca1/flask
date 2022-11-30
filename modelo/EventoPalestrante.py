from datetime import date, datetime

class EventoPalestrante:

    def __init__(self):

        self.__idpalestrante=""
        self.__idevento=""
        self.__idsemana=""
        self.__lista='idevento,idpalestrante,idsemana'

        self.__dadosInserir=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'eventoxpalestrante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.idevento, self.idpalestrante,self.idsemana)
        return self.__dadosInserir


    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idevento={} and idpalestrante={} and idsemana={}".format(self.idevento, self.idpalestrante, self.idsemana)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idaluno={}".format(self.idpalestrante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idpalestrante(self):
        return self.idpalestrante

    @idpalestrante.setter
    def idpalestrante(self, entrada):
        self.idpalestrante = entrada

    @property
    def idevento(self):
        return self.__idevento

    @idevento.setter
    def idevento(self,entrada):
        self.__idevento=entrada

    @property
    def idsemana(self):
        return self.__idsemana

    @idsemana.setter
    def idsemana(self,entrada):
        self.__idsemana=entrada

    @property
    def idpalestrante(self):
        return self.__idpalestrante

    @idpalestrante.setter
    def idpalestrante(self,entrada):
        self.__idpalestrante=entrada


    def __repr__(self):
        return  self.idevento

