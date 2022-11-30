from datetime import date, datetime

class Evento:

    def __init__(self):

        self.__idevento=""
        self.__nome=""
        self.__flag=0
        self.__descricao=""
        self.__data=""
        self.__horario=""
        self.__idsemana=""
        self.__local=""
        self.__idpalestrante=""
        self.__lista='nome,descricao,data,horario,idsemana,local,idpalestrante'

        self.__dadosInserir=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'evento'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}','{}','{}','{}','{}'".format(self.nome, self.descricao, self.data, self.horario, self.idsemana, self.local, self.idpalestrante)
        return self.__dadosInserir


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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, entrada):
        self.__descricao = entrada

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada    

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, entrada):
        self.__horario = entrada

    @property
    def idsemana(self):
        return self.__idsemana

    @idsemana.setter
    def idsemana(self, entrada):
        self.__idsemana = entrada   


    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, entrada):
        self.__local = entrada

    @property
    def idpalestrante(self):
        return self.__idpalestrante

    @idpalestrante.setter
    def idpalestrante(self, entrada):
        self.__idpalestrante = entrada              


    def __repr__(self):
        return  self.nome

