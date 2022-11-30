from datetime import date, datetime

class Palestrante:

    def __init__(self):

        self.__idpalestrante=""
        self.__nome=""
        self.__flag=0
        self.__email=""
        self.__cpf=""
        self.__lista='nome,email,cpf'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'palestrante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.nome, self.email,self.cpf)
        return self.__dadosInserir


    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idpalestrante={}".format(self.idpalestrante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idpalestrante={}".format(self.idpalestrante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idpalestrante(self):
        return self.__idpalestrante

    @idpalestrante.setter
    def idpalestrante(self, entrada):
        self.__idpalestrante = entrada

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, entrada):
        self.__email = entrada

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, entrada):
        self.__cpf = entrada



    def __repr__(self):
        return  self.nome

