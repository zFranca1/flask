from datetime import date, datetime

class Evento:

    def __init__(self):

        self.__idevento=""
        self.__nome=""
        self.__flag=0
        self.__palestrante=""
        self.__qtdvagas=""
        self.__lista='nome,palestrante,qtdvagas'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'evento'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.nome, self.palestrante,self.qtdvagas)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}',palestrante='{}' where idevento={}".format(self.nome, self.palestrante,self.idevento)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idevento={}".format(self.idevento)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from evento where idevento={}".format(self.idevento)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idevento(self):
        return self.__idevento

    @idevento.setter
    def idevento(self, entrada):
        self.__idevento = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, entrada):
        self.__flag = entrada

    @property
    def palestrante(self):
        return self.__palestrante

    @palestrante.setter
    def palestrante(self, entrada):
        self.__palestrante = entrada


    @property
    def qtdvagas(self):
        return self.__qtdvagas

    @qtdvagas.setter
    def qtdvagas(self, entrada):
        self.__qtdvagas = entrada


    def __repr__(self):
        return  self.nome

