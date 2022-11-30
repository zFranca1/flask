from datetime import date, datetime

class Semana:

    def __init__(self):

        self.__idsemana=""
        self.__nome=""
        self.__flag=0
        self.__local=""
        self.__datainicio=""
        self.__datatermino=""
        self.__descricao=""
        self.__lista='nome,local,datainicio,datatermino,descricao'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'semana'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}','{}','{}'".format(self.nome, self.local,self.datainicio, self.datatermino, self.descricao)
        return self.__dadosInserir


    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idsemana={}".format(self.idsemana)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idaluno={}".format(self.idsemana)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idsemana(self):
        return self.__idsemana

    @idsemana.setter
    def idsemana(self, entrada):
        self.__idsemana = entrada

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
    def local(self):
        return self.__local

    @local.setter
    def local(self, entrada):
        self.__local = entrada

    @property
    def datainicio(self):
        return self.__datainicio

    @datainicio.setter
    def datainicio(self, entrada):
        self.__datainicio = entrada

    @property
    def datatermino(self):
        return self.__datatermino

    @datatermino.setter
    def datatermino(self, entrada):
        self.__datatermino = entrada

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, entrada):
        self.__descricao = entrada         

    def __repr__(self):
        return  self.nome

